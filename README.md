# D2 Survivors Save Editor

A collection of community-made tools for editing save data in **D2 Survivors**.

Choose the tool that matches what you want to change: edit only your gold, or use the full GUI editor to modify gold and supported modifiers on equipped items.

> **Disclaimer:** This is an unofficial community project. It is not affiliated with or endorsed by the creators of D2 Survivors or Blizzard Entertainment. Use at your own risk and always back up your original save before making changes.

## Available Tools

### 1. Add Gold — No GUI

**Branch:** [`add-gold-no-gui`](https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/add-gold-no-gui)

A lightweight Python script for changing the saved gold amount without a graphical interface.

**Features**
- Edit the saved gold value.
- Process a save code beginning with `D2S1:`.
- Generate a modified save code.
- Write the result to `new_save.txt` without overwriting the original save.

**Tutorial:** [Watch the Add Gold — No GUI video](https://www.youtube.com/watch?v=Mg8NvlDRU30)

**Best for:** Users who prefer a simple script and do not need a graphical interface.

### 2. Add Gold — GUI

**Branch:** [`add-gold-gui`](https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/add-gold-gui)

A simple graphical application for editing gold only.

**Features**
- Paste a save code or use the clipboard.
- Load the save and view the current gold amount.
- Enter a new gold amount.
- Generate and copy the modified save code.
- Save the output to a separate text file.

**Tutorial:** [Watch the Add Gold — GUI video](https://www.youtube.com/watch?v=L1mKch2SIBA)

**Best for:** Users who want to edit gold through an easy-to-use window without changing item stats.

### 3. Item & Gold Editor — GUI

**Branch:** [`item-gold-editor-gui`](https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/item-gold-editor-gui)

A graphical save editor for changing gold and supported modifiers on equipped items across character classes.

**Features**
- Load a save code beginning with `D2S1:`.
- Edit the shared gold amount.
- Browse character classes and their equipped items.
- View and edit supported modifiers on equipped items.
- Preserve item edits when switching between items and classes.
- Generate a modified save code and save it to a separate file.

**Tutorial:** [Watch the Item & Gold Editor — GUI video](https://www.youtube.com/watch?v=J4QWHjDD6VQ)

**Best for:** Users who want to edit equipped item modifiers as well as gold.

## Requirements

- Windows
- Python 3.10 or newer
- A D2 Survivors save code beginning with `D2S1:`

The GUI versions use Python's Tkinter library. A standard Python installation that includes Tkinter should not need additional packages.

## Getting Started

1. Choose one of the tools above.
2. Open its branch.
3. Download the Python script listed in that branch's README.
4. Follow that tool's instructions.
5. Back up your original save, make your changes, and import the generated save code into the game.
6. Verify the result in-game before replacing or deleting any backup.

## Important

- Always keep a backup of your original save.
- The tools generate modified save output; check the instructions for the selected version.
- The available item modifiers depend on the data supported by the save and editor.
- This project is provided as-is, without guarantees.

## Author & Links

Created by **Just a Polish Guy**.

- **Main repository:** https://github.com/justPLguy/D2-Survivors-Save-Editor
- **YouTube channel:** https://www.youtube.com/@justPLguy

If you find the project useful, consider starring the repository ⭐
