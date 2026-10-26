#!/usr/bin/env python3
"""Checks that _data/tools.yml still matches the guides.

Run it from the repository root after changing a guide's headings or labels:

    python3 scripts/check_tools.py

It needs Python 3 and PyYAML. It exits with an error if anything in the ERRORS
list below is found, and prints NOTES for things worth knowing but not fatal.

ERRORS
  - an entry's guide file or anchor doesn't exist
  - an entry uses a platform, product, or label that isn't defined
  - a platform or product has no page in browse/
  - an entry's tags differ from the labels the guide shows for that section
  - a section in a guide has availability labels but no entry in tools.yml

NOTES
  - ids that appear twice on one page (a link goes to the first one)
"""
import collections
import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors, notes = [], []


def load(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return yaml.safe_load(f)


def slug(text):
    """The id kramdown gives a heading (letters, digits, and hyphens)."""
    text = re.sub(r"`", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"^[^a-zA-Z]+", "", text)
    text = re.sub(r"[^a-zA-Z0-9 -]", "", text)
    return text.replace(" ", "-").lower()


def read_lines(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read().split("\n")


def page_ids(lines):
    """Every id on a page, as a list of (id, line number)."""
    ids, used, in_code = [], collections.Counter(), False
    for number, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*(\{:\s*#([\w-]+)[^}]*\})?\s*#*$", line)
        if heading:
            if heading.group(4):
                ids.append((heading.group(4), number))
            else:
                base = slug(heading.group(2)) or "section"
                ids.append((base if used[base] == 0 else f"{base}-{used[base]}", number))
                used[base] += 1
        for match in re.finditer(r'<[a-zA-Z0-9]+[^>]*?\sid="([^"]+)"', line):
            ids.append((match.group(1), number))
    return ids


def includes(lines):
    """Every availability label line, as (line number, set of tags)."""
    found = []
    for number, line in enumerate(lines, 1):
        match = re.search(r'availability\.html tags="([^"]*)"', line)
        if match:
            found.append((number, set(match.group(1).split())))
    return found


def labelled_sections(lines, ids):
    """Headings and collapsed sections that have availability labels just under
    them. Returns (start line, end line, id or None, description)."""
    sections = []
    for number, _tags in includes(lines):
        for j in range(number - 1, max(-1, number - 8), -1):
            text = lines[j]
            heading = re.match(r"^(#{2,4}) (.+?)\s*(\{:.*\})?$", text)
            details = re.match(r"^\s*<details([^>]*)>", text)
            if heading:
                level = len(heading.group(1))
                end = len(lines)
                for k in range(j + 1, len(lines)):
                    later = re.match(r"^(#{1,4}) ", lines[k])
                    if later and len(later.group(1)) <= level:
                        end = k
                        break
                found = [i for i, n in ids if n == j + 1]
                sections.append((j + 1, end, found[0] if found else None, heading.group(2)))
                break
            if details:
                end = next((k for k in range(j, len(lines)) if "</details>" in lines[k]), len(lines) - 1)
                own_id = re.search(r'id="([^"]+)"', details.group(1))
                summary = next((re.search(r"<summary>(.*?)</summary>", lines[k]).group(1)
                                for k in range(j, min(len(lines), j + 3))
                                if re.search(r"<summary>(.*?)</summary>", lines[k])), "?")
                sections.append((j + 1, end + 1, own_id.group(1) if own_id else None, summary))
                break
        else:
            sections.append((0, len(lines) + 1, "", "the whole page"))
    return sections


def governing_tags(lines, anchor_line):
    """The labels the guide shows for a section: the labels within 5 lines after
    its anchor, otherwise the nearest ones before it."""
    labels = includes(lines)
    if not labels:
        return None
    if anchor_line == 0:
        return labels[0][1]
    after = [tags for n, tags in labels if anchor_line < n <= anchor_line + 5]
    if after:
        return after[0]
    before = [tags for n, tags in labels if n < anchor_line]
    return before[-1] if before else None


def main():
    tools = load("_data/tools.yml")
    browse = load("_data/browse.yml")
    labels = load("_data/availability.yml")
    platforms = {p["key"] for p in browse["platforms"]}
    products = {p["key"] for p in browse["products"]}

    for kind, folder, keys in (("platform", "browse/devices", platforms), ("product", "browse/software", products)):
        for key in sorted(keys):
            if not os.path.exists(os.path.join(ROOT, folder, f"{key}.md")):
                errors.append(f"browse.yml: the {kind} '{key}' has no page at {folder}/{key}.md")

    guides, id_lists = {}, {}
    for path in sorted(glob.glob(os.path.join(ROOT, "guides", "*.md"))):
        name = os.path.basename(path)[:-3]
        guides[name] = read_lines(f"guides/{name}.md")
        id_lists[name] = page_ids(guides[name])
        counts = collections.Counter(i for i, _ in id_lists[name])
        for i, count in counts.items():
            if count > 1:
                where = [n for k, n in id_lists[name] if k == i]
                notes.append(f"guides/{name}.md: id '{i}' is on lines {', '.join(map(str, where))}. Links go to the first.")

    entries_by_guide = collections.defaultdict(list)
    for index, tool in enumerate(tools, 1):
        label = f"tools.yml entry {index} ({tool.get('name')}, {tool.get('guide')})"
        guide = tool.get("guide")
        if guide not in guides:
            errors.append(f"{label}: there is no guides/{guide}.md")
            continue
        for key in tool.get("platforms") or []:
            if key not in platforms:
                errors.append(f"{label}: unknown platform '{key}'")
        for key in tool.get("products") or []:
            if key not in products:
                errors.append(f"{label}: unknown product '{key}'")
        tags = set((tool.get("tags") or "").split())
        for key in tags:
            if key not in labels:
                errors.append(f"{label}: unknown label '{key}'")

        anchor = tool.get("anchor")
        if anchor is None:
            errors.append(f"{label}: no anchor (use \"\" to link to the top of the page)")
            continue
        anchor_line = 0
        if anchor != "":
            line_numbers = [n for i, n in id_lists[guide] if i == anchor]
            if not line_numbers:
                errors.append(f"{label}: guides/{guide}.md has no heading or section with the id '{anchor}'")
                continue
            anchor_line = line_numbers[0]
        entries_by_guide[guide].append(anchor_line)

        shown = governing_tags(guides[guide], anchor_line)
        if shown is not None and shown != tags:
            errors.append(f"{label}: tags are '{' '.join(sorted(tags))}' but guides/{guide}.md "
                          f"shows '{' '.join(sorted(shown))}' (near line {anchor_line or 1})")

    for name, lines in guides.items():
        for start, end, section_id, description in labelled_sections(lines, id_lists[name]):
            if section_id is None:
                errors.append(f"guides/{name}.md line {start}: '{description}' has availability labels "
                              f"but no id, so it can't be linked to. Give it an id.")
            elif not any(start <= n < end or (start == 0 and n == 0) for n in entries_by_guide[name]):
                errors.append(f"guides/{name}.md line {start}: '{description}' has availability labels "
                              f"but no entry in tools.yml")

    for note in notes:
        print("NOTE:  ", note)
    for error in errors:
        print("ERROR: ", error)
    print(f"\n{len(tools)} entries checked: {len(errors)} errors, {len(notes)} notes.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
