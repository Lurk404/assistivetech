Display preferences (Fluid Infusion UI Options)
===============================================

This folder is a trimmed copy of Fluid Infusion 4.8.0, the files needed for
the "Show Preferences" panel at the top of every page.

  Source:   https://github.com/fluid-project/infusion  (npm package "infusion", version 4.8.0)
  Docs:     https://docs.fluidproject.org/infusion/development/UserInterfaceOptionsAPI
  Licence:  Infusion-LICENSE.txt (ECL 2.0 or BSD-3). The fonts in src/lib
            (Open Sans, OpenDyslexic, Atkinson Hyperlegible) are under the
            SIL Open Font License.

What's here
  infusion-uio.js                          Infusion + UI Options in one file (includes jQuery)
  src/framework/core/css/fluid.css         Small helper classes the panel uses
  src/framework/preferences/css/           Panel styles, and the styles that apply each preference
  src/framework/preferences/html/          Templates for each panel (loaded when the panel opens)
  src/framework/preferences/messages/      Panel wording, English only
  src/framework/preferences/fonts/         Icon font for the panel
  src/components/orator/                   Styles and icons for the text-to-speech play button
  src/lib/                                 Fonts readers can choose (OpenDyslexic, Atkinson Hyperlegible)
                                           and the panel's own font (Open Sans)

The files are unchanged from the release. Keep the folder layout as it is:
the CSS files find the fonts by relative paths (../../../lib/...).

Only the templates and wording for the eight panels in use are included
(text size, text style, line/letter/word spacing, contrast, enhance inputs,
text-to-speech), in English. If you add a panel in _includes/display_preferences.html (for
example "fluid.prefs.tableOfContents"), copy its template from html/ and its
wording from messages/ in the full Infusion download as well.

The site's own files that use this folder:
  _includes/head_custom.html               loads the CSS and infusion-uio.js
  _includes/display_preferences.html       the panel markup and the script that starts it
  _includes/header_custom.html             includes display_preferences.html
  _sass/custom/custom.scss                 "Display preferences" section: layout and fixes

To update Infusion later
  1. Download the new version: npm pack infusion  (or the release zip on GitHub)
  2. Copy the same files over the ones here, keeping the same paths.
  3. Update the version number above and test the panel on a few pages.
