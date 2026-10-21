# D2 Survivors Save Editor — GUI

A graphical save editor for **D2 Survivors**. Edit shared gold and supported modifiers on equipped items across different character classes.

**Created by Just a Polish Guy.**

> **Disclaimer:** This is an unofficial community-made project. It is not affiliated with or endorsed by the creators of D2 Survivors or Blizzard Entertainment. Use at your own risk and always back up your original save.

## Features

- Load a save code beginning with `D2S1:`.
- Edit the shared gold amount available across character classes.
- Browse character classes and their equipped items.
- View and edit supported modifiers on equipped items.
- Save item changes when switching between items and classes.
- Generate a modified save code.
- Save the output to a separate file without overwriting the original save.

## Requirements

- Windows
- Python 3.10 or newer
- A complete D2 Survivors save code beginning with `D2S1:`

The GUI uses Python's Tkinter library, included with standard Python installations that include Tkinter.

## How to Run

1. Download `item-gold-editor.py` from this branch.
2. Make sure Python 3.10 or newer is installed.
3. Open a terminal in the folder containing the file.
4. Run:

   ```bash
   py item-gold-editor.py
   ```

5. Paste your save code into the application or use **Paste from Clipboard**.
6. Click **Load Save Code**.
7. Select a character class and an equipped item.
8. Edit the supported modifiers and click **Save Item Changes**.
9. Click **Generate Modified Save**.
10. Copy the generated code or save the output to a file, then import it into the game and verify the result.

## Video Tutorial

▶️ **Watch the Item & Gold Editor — GUI tutorial:**  
https://www.youtube.com/watch?v=J4QWHjDD6VQ

## Important

**Always back up your original save before making changes.** Available modifiers depend on the save data and the fields supported by the editor. Verify the modified save in-game.

## Other Tools

- **Main repository:** https://github.com/justPLguy/D2-Survivors-Save-Editor
- **Add Gold — No GUI:** https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/add-gold-no-gui
- **Add Gold — GUI:** https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/add-gold-gui

## Credits

Created and maintained by **Just a Polish Guy**.

YouTube channel: https://www.youtube.com/@justPLguy

This is an unofficial community project and is not affiliated with or endorsed by the creators of D2 Survivors or Blizzard Entertainment.
