---
title: Screen Readers
nav_order: 12
---

# Screen Readers

<img src="../assets/images/screen-readers/screen-readers-icon.png" alt="" width="211"> <!-- review-alt -->

**On this page:**

- [JAWS](#jaws)
- [NVDA](#nvda)
- [VoiceOver](#voiceover)
- [TalkBack](#talkback)
- [ChromeVox](#chromevox-chromeos)

## JAWS

JAWS (Job Access With Speech) is the most popular screen reader software. JAWS is available only for Windows but allows almost every function of Windows to be performed with only the use of a keyboard and audio feedback. JAWS is a very expensive (~$1000USD) and complicated piece of software, but indispensable for blind or low vision students. [Download JAWS from Freedom Scientific](https://support.freedomscientific.com/Downloads/JAWS).

<details markdown="block">
<summary>Common JAWS commands</summary>

This guide uses <kbd>JAWS</kbd> to indicate the modifier key, which could be either <kbd>Caps Lock</kbd> or <kbd>Insert</kbd> depending on the user’s computer and keyboard layout.

| Action | Key command |
| --- | --- |
| Contextual Help (overview of website or document, such as headings, links, etc.) | <kbd>JAWS</kbd> + <kbd>F1</kbd> |
| View contextual JAWS hotkeys | <kbd>Insert</kbd> + <kbd>B</kbd> (this control is Insert regardless of keyboard setup) |
| Show list of all buttons, frames, graphics, lists, links, etc. | <kbd>JAWS</kbd> + <kbd>F3</kbd> |
| Buttons list | <kbd>Ctrl</kbd> + <kbd>JAWS</kbd> + <kbd>B</kbd> |
| Form elements (fields, radio buttons, checkboxes, etc.) list | <kbd>JAWS</kbd> + <kbd>F5</kbd> |
| Headings list | <kbd>JAWS</kbd> + <kbd>F6</kbd> |
| Links list | <kbd>JAWS</kbd> + <kbd>F7</kbd> |
| Frames list | <kbd>JAWS</kbd> + <kbd>F9</kbd> |
| Start reading continuously from current point | <kbd>JAWS</kbd> + <kbd>Down Arrow</kbd> |
| Stop reading | <kbd>Ctrl</kbd> |
| Read next item | <kbd>Down Arrow</kbd> |
| Move to next/previous paragraph | <kbd>P</kbd> / <kbd>Shift</kbd> + <kbd>P</kbd> |
| Move to next/previous focusable item (link, button, text field, etc.) | <kbd>Tab</kbd> / <kbd>Shift</kbd> + <kbd>Tab</kbd> |
| Activate link or button | <kbd>Enter</kbd> |
| Move to next/previous heading | <kbd>H</kbd> / <kbd>Shift</kbd> + <kbd>H</kbd> |
| Move to main content region | <kbd>Q</kbd> |
| Move to next/previous region | <kbd>R</kbd> / <kbd>Shift</kbd> + <kbd>R</kbd> |
| Next/previous radio button | <kbd>A</kbd> / <kbd>Shift</kbd> + <kbd>A</kbd> |
| Next/previous frame | <kbd>M</kbd> / <kbd>Shift</kbd> + <kbd>M</kbd> |
| Toggle Virtual Cursor on/off | <kbd>JAWS</kbd> + <kbd>Z</kbd> |
| Refresh screen without reloading page | <kbd>JAWS</kbd> + <kbd>Escape</kbd> |
| Speech history (last 100 items read by JAWS) | <kbd>JAWS</kbd> + <kbd>Space</kbd>, then <kbd>H</kbd> |

This is not an extensive list of JAWS keystrokes.

</details>

<details markdown="block">
<summary>Virtual Viewer</summary>

Press <kbd>JAWS</kbd> + <kbd>Alt</kbd> + <kbd>W</kbd> to open the virtual viewer of the current window. This provides all the text on screen in a line-by-line format that may be easier to navigate or review for messages or codes.

Press <kbd>JAWS</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> to open the virtual viewer of the current control, such as a pop-up or notification. This provides all the text in the current control in a line-by-line format that may be easier to navigate or review for messages or codes.

</details>

<details markdown="block">
<summary>Forms Mode</summary>

When navigating into a properly coded form (on the web, in a PDF) JAWS switches to Forms mode, and a sound will play indicating the change. This mode disables many JAWS keystrokes so users can enter text into the form. If users need to enter forms mode, press <kbd>Enter</kbd> when focused on a form field. Press <kbd>Num Pad Plus</kbd> (which may be **function ?** on laptop keyboards) to exit forms mode.

</details>

<details markdown="block">
<summary>PDFs</summary>

A properly tagged PDF can be navigated by a JAWS user just like they navigate a webpage using headings (press <kbd>H</kbd>), tables (press <kbd>T</kbd>), and links (press <kbd>JAWS</kbd> + <kbd>F7</kbd>). PDFs can be awkward to read with JAWS. Try pressing <kbd>Alt</kbd> + <kbd>Tab</kbd> until the PDF is focused and press <kbd>JAWS</kbd> + <kbd>B</kbd> to begin reading the current window.

</details>

<details markdown="block">
<summary>Convenient OCR</summary>

If JAWS indicates a PDF is empty, it likely means it is an inaccessible PDF (image of text). JAWS has a built-in optical character recognition tool to extract text from an image and display it in a format readable by JAWS users. To use Convenient OCR:

1. Open a PDF.
2. JAWS should indicate if the PDF is inaccessible and prompt users to use **Convenient OCR**. <kbd>Tab</kbd> to **Yes** and press <kbd>Enter</kbd>.
3. If JAWS does not prompt the user, or the dialogue is accidentally closed, press <kbd>JAWS</kbd> + <kbd>Space</kbd>, then <kbd>O</kbd> followed by <kbd>D</kbd>. This will start the Convenient OCR tool.
4. When the document is displayed in JAWS Virtual Viewer, press <kbd>Tab</kbd> to **Open in Word** and press <kbd>Enter</kbd> to view the document in Word.

See [Optical Character Recognition](optical-character-recognition.md) for other OCR tools.

</details>

<details markdown="block">
<summary>PlaceMarkers</summary>

For frequently visited websites, users may consider using PlaceMarkers for efficient navigation. Move to the place on the page you want to return to, press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>K</kbd> and then <kbd>Enter</kbd> on the **Add** button. When returning to the page, press <kbd>K</kbd> to cycle through PlaceMarkers or press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>K</kbd> to see a list of PlaceMarkers.

</details>

<details markdown="block">
<summary>Ignore next key press</summary>

When encountering something that should be keyboard navigable (for example, instructions read “press left or right arrow to move through content”), press <kbd>JAWS</kbd> + <kbd>3</kbd> then the left or right arrow. <kbd>JAWS</kbd> + <kbd>3</kbd> tells JAWS to ignore the next key press and allows navigation of web content as if JAWS weren’t running.

</details>

<details markdown="block">
<summary>General Windows Keyboard Commands</summary>

In addition to JAWS commands, there are some Windows keyboard shortcuts that may help users.

- <kbd>Ctrl</kbd> + <kbd>F</kbd> to search in a webpage or document.
- <kbd>Alt</kbd> + <kbd>Tab</kbd> to move between open windows.
- <kbd>Windows</kbd> + <kbd>D</kbd> moves to the desktop. From the desktop, <kbd>Windows</kbd> + <kbd>D</kbd> moves focus back to the previous window.
- <kbd>Windows</kbd> + <kbd>T</kbd> moves to the taskbar. <kbd>Windows</kbd> and a number opens or moves to that taskbar item.
- Press the <kbd>Windows</kbd> key and type to search the computer.

</details>

<details markdown="block">
<summary>Links</summary>

- [Freedom Scientific JAWS guide to web browsing](https://www.freedomscientific.com/training/jaws/hotkeys)
- Freedom Scientific [complete list of JAWS keystrokes](https://www.freedomscientific.com/Content/Documents/Manuals/JAWS/Keystrokes.pdf)
- [Web Accessibility in Mind Keyboard Shortcuts for JAWS](https://webaim.org/resources/shortcuts/jaws)
- Deque University [JAWS Keyboard Shortcuts](https://dequeuniversity.com/screenreaders/jaws-keyboard-shortcuts)
- JAWS has a [webpage for JAWS users to learn](https://www.freedomscientific.com/SurfsUp/_Surfs_Up_Start_Here.htm) about and practice surfing the web.
- Portland Community College has a helpful guide to [navigating D2L with JAWS](https://www.pcc.edu/instructional-support/accessibility/resources/jaws/d2l).
- Cracking the Code, [Reading PDFs with JAWS](https://doccenter.freedomscientific.com/doccenter/archives/2021_04_15_Tips_for_Reading_PDFs_with_JAWS/Cracking_the_Code_Reading_PDFs_with_JAWS_Resource_File.pdf)
- General [screen reader shortcuts](https://www.a11yproject.com/posts/learning-common-keyboard-shortcuts-for-screen-readers)

</details>

## NVDA

NVDA is a free and open-source screen reader. NVDA is available for Windows only. NVDA is second to JAWS in usage, but has many similar features. [Download NVDA](https://www.nvaccess.org/download) from nvaccess.org.

The first time NVDA is started, it will prompt users to set various settings (auto start, user settings, etc.) and, most importantly, the NVDA key. This guide will list <kbd>NVDA</kbd> as the modifier key, which will refer to whichever key the user chooses (<kbd>Caps Lock</kbd>, <kbd>Insert</kbd>, and <kbd>Num Pad Insert</kbd> are available options).

<details markdown="block">
<summary>Common NVDA commands</summary>

| Action | Keystroke |
| --- | --- |
| Open NVDA | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>N</kbd> |
| Close NVDA | <kbd>NVDA</kbd> + <kbd>Q</kbd>, and <kbd>Enter</kbd> to confirm |
| Change speech mode (off, beeps, talk) | <kbd>NVDA</kbd> + <kbd>S</kbd> |
| Open NVDA menu | <kbd>NVDA</kbd> + <kbd>N</kbd> |
| Preferences | (With NVDA menu open) <kbd>P</kbd> |
| Tools | (With NVDA menu open) <kbd>T</kbd> |
| Help | <kbd>NVDA</kbd> + <kbd>1</kbd> |
| Read from current position | <kbd>NVDA</kbd> + <kbd>Down Arrow</kbd> |
| Read current line | <kbd>NVDA</kbd> + <kbd>Up Arrow</kbd> |
| Read previous/next word | <kbd>Ctrl</kbd> + <kbd>Left Arrow</kbd> / <kbd>Right Arrow</kbd> |
| Read previous/next paragraph | <kbd>Ctrl</kbd> + <kbd>Up Arrow</kbd> / <kbd>Down Arrow</kbd> |
| Read next item | <kbd>Down Arrow</kbd> |
| Stop reading | <kbd>Ctrl</kbd> |
| Pause/resume reading | <kbd>Shift</kbd> |
| Change rate of speech | <kbd>NVDA</kbd> + <kbd>Shift</kbd> + <kbd>Ctrl</kbd> + <kbd>Up Arrow</kbd> / <kbd>Down Arrow</kbd> |
| Input help (announces button but takes no action) | <kbd>NVDA</kbd> + <kbd>1</kbd> |
| Elements (links, headings, buttons, etc.) window | <kbd>NVDA</kbd> + <kbd>F7</kbd> |
| Move between elements lists | <kbd>Tab</kbd> |
| Move between focusable elements (links, buttons, forms, menus) | <kbd>Tab</kbd> / <kbd>Shift</kbd> + <kbd>Tab</kbd> |
| Next heading | <kbd>H</kbd> |
| Heading level 1-6 | <kbd>1</kbd> to <kbd>6</kbd> |
| Next link | <kbd>K</kbd> |
| Next unvisited link | <kbd>U</kbd> |
| Next visited link | <kbd>V</kbd> |
| Next landmark/region | <kbd>D</kbd> |
| Next form field | <kbd>F</kbd> |
| Next text field | <kbd>E</kbd> |
| Next checkbox | <kbd>X</kbd> |
| Next radio button | <kbd>R</kbd> |
| Open combo box | <kbd>Alt</kbd> + <kbd>Down Arrow</kbd> |
| Next table | <kbd>T</kbd> |
| Navigate table cells | <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + arrow keys |
| Next button | <kbd>B</kbd> |
| Next list | <kbd>L</kbd> |
| Next list item | <kbd>I</kbd> |
| Next image | <kbd>G</kbd> |
| Move to previous instance | <kbd>Shift</kbd> + any of the single keystrokes above |
| Search | <kbd>NVDA</kbd> + <kbd>Ctrl</kbd> + <kbd>F</kbd> |
| Move to next/previous search result | <kbd>NVDA</kbd> + <kbd>F3</kbd> / <kbd>NVDA</kbd> + <kbd>Shift</kbd> + <kbd>F3</kbd> |
| Focus mode (NVDA keystrokes ignored) | <kbd>NVDA</kbd> + <kbd>Space</kbd> |
| Browse mode (regular NVDA behaviour) | <kbd>NVDA</kbd> + <kbd>Space</kbd> |
| Ignore next key press | <kbd>NVDA</kbd> + <kbd>F2</kbd> |

</details>

<details markdown="block">
<summary>General Windows Keyboard Commands</summary>

In addition to NVDA commands, there are some Windows keyboard shortcuts that may help users.

- <kbd>Ctrl</kbd> + <kbd>F</kbd> to search in a webpage or document.
- <kbd>Alt</kbd> + <kbd>Tab</kbd> to move between open windows.
- <kbd>Windows</kbd> + <kbd>D</kbd> moves to the desktop. From the desktop, <kbd>Windows</kbd> + <kbd>D</kbd> moves focus back to the previous window.
- <kbd>Windows</kbd> + <kbd>T</kbd> moves to the taskbar. <kbd>Windows</kbd> and a number opens or moves to that taskbar item.
- Press the <kbd>Windows</kbd> key and type to search the computer.

</details>

<details markdown="block">
<summary>Links</summary>

- Web Accessibility in Mind [introduction to NVDA](https://webaim.org/articles/nvda)
- Web Accessibility in Mind list of [NVDA keyboard shortcuts](https://webaim.org/resources/shortcuts/nvda)
- A11y Project [getting started with NVDA](https://www.a11yproject.com/posts/getting-started-with-nvda)
- [NVDA official user guide](https://www.nvaccess.org/files/nvda/documentation/userGuide.html)

</details>

## VoiceOver

VoiceOver is a screen reader built into macOS and iOS.

<details markdown="block">
<summary>VoiceOver on macOS</summary>

To activate VoiceOver on macOS:

1. Navigate to **System Settings > Accessibility**.
2. Choose **VoiceOver**.
3. Toggle **VoiceOver** on.
   1. Alternatively, VoiceOver can be toggled using <kbd>Command</kbd> + <kbd>F5</kbd>.

Click **Open VoiceOver Training…** for help and training.

Click **Open VoiceOver Utility…**, or press <kbd>Control</kbd> + <kbd>Option</kbd> + <kbd>F8</kbd> when VoiceOver is running, to open the options and settings screen for VoiceOver, allowing users to change speech, sound, and keyboard shortcuts.

The default VoiceOver modifier keys are <kbd>Control</kbd> + <kbd>Option</kbd>. In the following, <kbd>VO</kbd> means pressing <kbd>Control</kbd> + <kbd>Option</kbd>.

\*VoiceOver requires multiple modifier keys as it works within the existing macOS system.

| Action | Keystroke |
| --- | --- |
| Open Rotor to display headings, links, regions, etc. lists | <kbd>VO</kbd> + <kbd>U</kbd> |
| Start reading | <kbd>VO</kbd> + <kbd>A</kbd> |
| Stop reading | <kbd>Control</kbd> |
| Next | <kbd>VO</kbd> + <kbd>Right Arrow</kbd> |
| Previous | <kbd>VO</kbd> + <kbd>Left Arrow</kbd> |
| Next paragraph | <kbd>VO</kbd> + <kbd>P</kbd> |
| Next link | <kbd>VO</kbd> + <kbd>Command</kbd> + <kbd>L</kbd> |
| Next heading | <kbd>VO</kbd> + <kbd>Command</kbd> + <kbd>H</kbd> |
| Move to table | <kbd>VO</kbd> + <kbd>Command</kbd> + <kbd>T</kbd> |
| Activate focused element | <kbd>VO</kbd> + <kbd>Space</kbd> |
| Next link, form field, button, etc. | <kbd>Tab</kbd> |
| Previous link, form field, etc. | <kbd>Shift</kbd> + <kbd>Tab</kbd> |

\*VoiceOver works best with Safari when browsing the internet.

Users may consider using [VoiceOver Quick Nav](https://support.apple.com/en-ca/guide/voiceover/vo27943/mac), which allows users to skip pressing the VO key combination. To enable this setting:

1. Navigate to **System Settings**.
2. Choose **Accessibility**.
3. Select **VoiceOver**.
4. Select **Open VoiceOver Utility…**
5. Move to **Commanders** in the sidebar.
6. Move to the **Quick Nav** tab.
7. Check **Enable arrow-key Quick Nav** and **Enable single-key Quick Nav**.

- [Complete list of VoiceOver commands](https://www.apple.com/voiceover/info/guide/_1131.html)
- [VoiceOver User Guide](https://support.apple.com/en-ca/guide/voiceover/welcome/mac)
- [Getting started with macOS VoiceOver](https://www.a11yproject.com/posts/getting-started-with-voiceover)
- [WebAIM VoiceOver guide](https://webaim.org/articles/voiceover)

</details>

<details markdown="block">
<summary>VoiceOver on iPhone</summary>

To turn on VoiceOver:

1. Navigate to **Settings**.
2. Choose **Accessibility**.
3. Tap **VoiceOver**.
4. Toggle **VoiceOver** on.
   1. Various settings are available. Select **Speech** and then **Voice** to set voice options.

### Using VoiceOver

VoiceOver has a practice area where you can try out different gestures and VoiceOver will announce the gesture and what action that gesture does.

1. Navigate to **Settings > Accessibility**.
2. With VoiceOver on, select **VoiceOver Practice**.

- Tap anywhere on the screen to have an item read aloud.
- Drag a finger to move between items.
- Swipe right to read next, swipe left to read previous.
- Twist two fingers on the screen to open the rotor.
  - The rotor allows users to navigate by headings, links, words, or other controls.
  - Swipe up or down to navigate by the chosen navigation type.
- Tap on an element to select it, double tap to activate.
- Tap with two fingers to pause VoiceOver.
- Swipe up from the bottom to return to Home, and keep dragging up to go to the App Switcher.
  - Flick left or right with three fingers to move between apps.
  - Flick three fingers up to close an app.

[Use Voice Control to interact with iPhone](https://support.apple.com/en-ca/guide/iphone/iph2c21a3c88/ios)

[AppleVis](https://www.applevis.com) is a resource for blind and low vision users of Apple products.

</details>

## TalkBack

TalkBack is the default screen reader for Android.

<details markdown="block">
<summary>Using TalkBack</summary>

To enable TalkBack:

1. Navigate to **Settings > Accessibility**.
2. Turn **TalkBack** on and toggle **TalkBack shortcut** to on.
   1. With the shortcut on, hold the up and down volume buttons to turn TalkBack on.
3. The first time TalkBack is turned on, a tutorial opens.

Using TalkBack:

- Swipe right to read next, swipe left to read previous.
- Tap on the screen to read a specific item.
  - Tap and drag to move reading focus around the page.
- Double tap to select a link, use a button, or open a menu.
- Swipe down and up in one motion to cycle navigation options such as headings, controls, or links.
  - Swipe up or down to move between the selected element type.

TalkBack has a practice area where you can try out different gestures and TalkBack will announce the gesture and what action that gesture does. To use the practice tool:

1. Navigate to **TalkBack**.
2. Choose **TalkBack Settings > Tutorial and help > Practice gestures**.

[TalkBack getting started guide](https://support.google.com/accessibility/android/topic/10601570?hl=en&ref_topic=3529932&sjid=2464805182940270078-NC)

</details>

## ChromeVox (ChromeOS)

ChromeVox is the built-in screen reader on Chromebooks.

<details markdown="block">
<summary>Using ChromeVox</summary>

Toggle ChromeVox on or off by pressing <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Z</kbd>.

To open the ChromeVox menu, press <kbd>Search</kbd>.

The ChromeVox menu includes menus for speech options and help as well as lists of headings, landmarks, links, form controls, and tables.

| Action | Keystroke |
| --- | --- |
| Start reading from current location | <kbd>Search</kbd> + <kbd>R</kbd> |
| Go to top of page | <kbd>Search</kbd> + <kbd>Ctrl</kbd> + <kbd>Left Arrow</kbd> |
| Read next line | <kbd>Search</kbd> + <kbd>Down Arrow</kbd> |
| Read next word | <kbd>Search</kbd> + <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Right Arrow</kbd> |
| Move to next heading | <kbd>Search</kbd> + <kbd>H</kbd> |
| Move to next link | <kbd>Search</kbd> + <kbd>L</kbd> |
| Move to next landmark | <kbd>Search</kbd> + <kbd>;</kbd> |
| Move to previous heading/link/landmark | <kbd>Shift</kbd> + <kbd>Search</kbd> + <kbd>H</kbd>, <kbd>L</kbd> or <kbd>;</kbd> |
| Show heading list | <kbd>Search</kbd> + <kbd>Ctrl</kbd> + <kbd>H</kbd> |
| Show links list | <kbd>Search</kbd> + <kbd>Ctrl</kbd> + <kbd>L</kbd> |
| Show landmark list | <kbd>Search</kbd> + <kbd>Ctrl</kbd> + <kbd>;</kbd> |

[ChromeVox user guide](https://support.google.com/chromebook/answer/7031755?hl=en)

</details>

---

*Assistive Technology User Guides* by Luke McKnight is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
