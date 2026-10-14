# AT User Guides

Guides to assistive technology tools and strategies: text to speech, speech to text, screen readers, magnifiers, captions, OCR, mind mapping and more. Originally published in Pressbooks as *Assistive Technology User Guides* by Luke McKnight.

- **Website:** https://lurk404.github.io/assistivetech/
- **Wiki:** https://github.com/Lurk404/assistivetech/wiki

## What's in this repository

| Path | Contents |
| --- | --- |
| `index.md` | Home page of the website |
| `guides/` | One Markdown file per guide |
| `using-this-resource.md`, `accessibility-statement.md` | About pages |
| `assets/images/<guide>/` | Screenshots for each guide, in a folder named after the guide |
| `assets/images/logos/` | Product and operating system logos used on one or more pages |
| `_config.yml` | Website settings (title, theme, search, callouts) |
| `_sass/custom/custom.scss` | Extra styles for collapsible sections and keyboard keys |

## Editing a guide

Each guide starts with a few lines of front matter:

```yaml
---
title: Morphic
nav_order: 14
---
```

`title` is the name in the website menu and `nav_order` is its position.

Collapsible sections use the HTML `<details>` element. Keep the blank lines so the Markdown inside is formatted both here and on the website:

```html
<details markdown="block">
<summary>Section title</summary>

Markdown content here.

</details>
```

Keyboard keys use `<kbd>`, for example `<kbd>Ctrl</kbd> + <kbd>C</kbd>`.

Images use paths relative to the page, for example `../assets/images/morphic/morphicbar.jpg` from a file in `guides/`. Every image has alt text or an empty alt (`![]()`) if it's decorative. The `<!-- review-alt -->` comments mark alt text drafted during the move from Pressbooks; delete them once it's been checked.

## Licence

*Assistive Technology User Guides* by Luke McKnight is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
