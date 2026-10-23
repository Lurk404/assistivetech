# Maintaining the Browse by pages

The **Browse by Device or System** and **Browse by Software** pages are built from one data file, `_data/tools.yml`. Each entry points to a tool's section in a guide. `scripts/check_tools.py` checks that the data still matches the guides.

The work is the same each time: edit the guide, add or update an entry, run the checker, preview, merge.

## How it fits together

| File | What it does |
| --- | --- |
| `_data/tools.yml` | One entry for each tool or feature section in the guides |
| `_data/browse.yml` | The devices and software that have a Browse by page |
| `_data/availability.yml` | The availability labels (Built in, Free, Paid, and so on) |
| `browse/devices/` and `browse/software/` | One small page for each device or software, which filters `tools.yml` |
| `_includes/tool-index.html` | Builds the list on each device or software page |
| `_includes/browse-section.html` | The introduction and list of pages. Used on the Browse by pages and in the home page accordions |
| `scripts/check_tools.py` | Checks `tools.yml` against the guides |

## Before you start

- [ ] Work in a branch, not on `main`: `git switch -c my-change`
- [ ] Python 3 and PyYAML are installed (`py -m pip install pyyaml`; on Mac or Linux use `python3`)

## Add or change a tool section (for example, a new Word feature)

An entry is needed for each tool section that has availability labels under its heading. A new tip inside an existing section needs nothing.

- [ ] **Write the section in the guide.** Give it a heading or a `<details id="...">`, with the availability labels directly under it.
- [ ] **Add an entry to `_data/tools.yml`.** Put it inside that guide's group, in the same order as the page. For example:

  ```yaml
  - name: Word Read Aloud settings
    guide: text-to-speech-tools
    anchor: word-read-aloud-settings
    tags: langara paid
    platforms: [windows, macos]
    products: [word]
    summary: "Change the voice and reading speed."
  ```

- [ ] **Match the guide.** `tags` must be the same labels the guide shows for that section.
- [ ] **List only platforms the guide names.** If it doesn't say, leave `platforms` out. The tool will appear on its software page but on no device page.
- [ ] **Use `anchor: ""`** to link to the top of the page instead of a section.
- [ ] **Run the checker** (see below) and fix any errors.
- [ ] **Preview**, then merge.

## Add a platform (for example, Linux)

- [ ] **Register it.** Add it under `platforms:` in `_data/browse.yml`:

  ```yaml
  - key: linux
    title: Linux
    description: tools that run on Linux.
  ```

- [ ] **Create its page.** Copy `browse/devices/android.md` to `browse/devices/linux.md`. Change the `title`, the `nav_order`, and the include to `platform="linux"`. Web is currently 6, so give Linux 6 and change `browse/devices/web.md` to 7 if you want Web last.
- [ ] **Add the platform to existing entries.** Calibre and Audapolis already say they work on Linux in the guides. Add `linux` to their `platforms` lists.
- [ ] **Add any new Linux tools** as above, with `platforms: [linux]`.
- [ ] **Run the checker.** It errors if a platform in `browse.yml` has no page, or if an entry uses a platform that isn't registered.
- [ ] The home page accordion and the By Device or System list update on their own. Nothing else needs editing.

## Add a software page

Add one when a tool or vendor appears in more than one guide.

- [ ] **Register it.** Add it under `products:` in `_data/browse.yml`, with a `key`, `title`, and `description`.
- [ ] **Create its page.** Copy a page in `browse/software/`. Change the `title`, the `nav_order`, and the include to `product="your-key"`.
- [ ] **Add the key** to the `products` list of each entry that belongs to it.
- [ ] **Avoid a title that matches a guide.** Two pages with the same title are confusing in the menu and in search.
- [ ] **Run the checker.**

## Rename, move, or delete a heading in a guide

- [ ] **Update the entry's `anchor`** in `tools.yml` to the new id. Links to the old one stop working.
- [ ] **Deleting a section?** Delete its entry too.
- [ ] **Changed the availability labels?** Change the entry's `tags` to match.
- [ ] **Run the checker.**

## Run the checker

From the top folder of the repository:

```bash
py scripts/check_tools.py
```

On Mac or Linux, use `python3` instead of `py`. A clean run ends with `0 errors`.

**Errors** must be fixed. They mean one of these:

- an entry points to a guide or anchor that doesn't exist
- an entry uses a platform, software key, or label that isn't defined
- a platform or software page is missing
- an entry's tags differ from what the guide shows
- a section with availability labels has no entry, or has no id to link to

**Notes** are worth knowing but don't fail the check:

- ids that appear twice on one page, where links go to the first one
- entries with no platforms or products, so they appear on no Browse by page

## Before you merge

- [ ] The checker reports `0 errors`.
- [ ] The Browse page for the device or software you changed shows the new or changed tool.
- [ ] Its link goes to the right section in the guide, and opens it if it's collapsed.
- [ ] The label popovers open on the Browse page.
- [ ] The home page accordions still list every device and software.

## Good to know

- The checker only runs when you run it. It isn't part of the monthly link check.
- The Browse by lists are only as complete as `tools.yml`. A tool that's in a guide but not in `tools.yml` won't be listed.
- The summaries are written by hand. When a guide changes what a tool does, update the entry's `summary` too.
