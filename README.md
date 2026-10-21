# D2 Survivors — Add Gold GUI

A simple graphical tool for editing your gold in **D2 Survivors**.

No command line and no item-stat editing: load your save, enter the gold amount you want, and generate a modified save code.

**Created by Just a Polish Guy.**

> **Disclaimer:** This is an unofficial community project. It is not affiliated with or endorsed by the creators of D2 Survivors or Blizzard Entertainment. Use at your own risk and always back up your original save.

## Features

- **Simple GUI** — use a window instead of the command line.
- **Load Save Code** — paste a complete `D2S1:` save code into the application.
- **Clipboard support** — paste the code from your clipboard.
- **View Current Gold** — see the gold amount found in the loaded save.
- **Edit Gold** — enter a new gold amount.
- **Generate Modified Save** — create the updated save code.
- **Copy Output** — copy the generated code to the clipboard.
- **Save to File** — export the generated code to a separate `.txt` file.

## Requirements

- Windows
- Python 3.10 or newer
- A complete D2 Survivors save code beginning with `D2S1:`

The application uses Python's Tkinter library, which is included with standard Python installations that include Tkinter.

## How to Use

1. Download `d2_survivors_gold_editor_gui.py` from this branch.
2. Run the program:

   ```bash
   py d2_survivors_gold_editor_gui.py
   ```

3. Copy your save code from D2 Survivors.
4. Paste the code into the application or click **Paste from Clipboard**.
5. Click **Load Save Code**.
6. Enter your desired gold amount.
7. Click **Generate Modified Save**.
8. Copy the generated code or save it to a `.txt` file.
9. Import the modified save code into the game and verify the result.

## Video Tutorial

▶️ **Watch the Add Gold — GUI tutorial:**  
https://www.youtube.com/watch?v=L1mKch2SIBA

## Important

**Back up your original save before making any changes.** The editor creates modified output rather than intentionally overwriting your original save. Always verify the result in-game.

## Other Tools

- **Main repository:** https://github.com/justPLguy/D2-Survivors-Save-Editor
- **Add Gold — No GUI:** https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/add-gold-no-gui
- **Item & Gold Editor — GUI:** https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/item-gold-editor-gui

## Credits

Created by **Just a Polish Guy**.

YouTube channel: https://www.youtube.com/@justPLguy

This is an unofficial community project and is not affiliated with or endorsed by the creators of D2 Survivors or Blizzard Entertainment.
