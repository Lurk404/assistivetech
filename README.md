# AT User Guides

Guides to assistive technology tools and strategies: text to speech, speech to text, screen readers, magnifiers, captions, OCR, mind mapping and more. Originally published in Pressbooks as *Assistive Technology User Guides* by Luke McKnight.

[View the guides](https://lurk404.github.io/assistivetech/)

## What's in this repository

| Path | Contents |
| --- | --- |
| `index.md` | Home page of the website |
| `guides/` | One Markdown file per guide, plus the four group pages (`reading.md`, `writing-and-notes.md`, `seeing-and-hearing.md`, `more-tools.md`) |
| `about/` | About pages: Using This Resource and the Accessibility Statement |
| `assets/images/<guide>/` | Screenshots for each guide, in a folder named after the guide |
| `assets/images/logos/` | Product and operating system logos used on one or more pages |
| `_config.yml` | Website settings (title, theme, search, callouts) |
| `_data/availability.yml` | Wording and colour of the availability labels |
| `_includes/` | Additions to the theme: availability labels, display preferences, the light/dark button, the floating "On this page" and "Back to top" buttons, and the external link icons |
| `_sass/custom/custom.scss` | Extra styles. The comment at the top lists its sections |

## Editing a guide

Each guide starts with a few lines of front matter:

```yaml
---
title: Morphic
parent: More Tools
nav_order: 2
---
```

`title` is the name in the website menu and `nav_order` is its position. Guides are grouped in the menu under four parent pages in `guides/` (Reading, Writing and Notes, Seeing and Hearing, More Tools): `parent:` must match the parent page's `title`, and `nav_order` is the position within the group. When you add or move a guide, also update the grouped list on the home page (`index.md`).

### Accordions

Collapsible sections use the HTML `<details>` element. Keep the blank lines so the Markdown inside is formatted both here and on the website:

```html
<details markdown="block">
<summary>Section title</summary>

Markdown content here.

</details>
```

### Keyboard keys

Keyboard keys use `<kbd>`, for example `<kbd>Ctrl</kbd> + <kbd>C</kbd>`.

### Boxes

Callout boxes use a line like `{: .note }` or `{: .tip }` or `{: .warning }` directly above a paragraph (see `_config.yml`). On the website the paragraph becomes a coloured box; in the GitHub view the `{: .note }` line shows as plain text.

### Images

Images use paths relative to the page, for example `../assets/images/morphic/morphicbar.jpg` from a file in `guides/`. On the website every image sits on its own line. For a small icon in the middle of a sentence, use `<img class="inline" src="..." alt="..." width="30">` instead. Every image has alt text or an empty alt (`![]()`) if it's decorative. The `<!-- review-alt -->` comments mark alt text drafted during the move from Pressbooks; delete them once it's been checked.

Put each screenshot on its own line under the step it belongs to. Inside a numbered step, indent it 3 spaces so it stays part of that step.

Use `<img src="../assets/images/closed-captions/kaltura-cc-button.png" alt="..." width="...">` 

## Licence

*Assistive Technology User Guides* by Luke McKnight is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
