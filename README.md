# Add Gold — No GUI

A lightweight command-line Python tool for changing the saved gold value in **D2 Survivors**.

**Created by Just a Polish Guy.**

> **Disclaimer:** This is an unofficial community-made tool. It is not affiliated with or endorsed by the creators of D2 Survivors or Blizzard Entertainment. Use at your own risk and always back up your original save.

## Features

- Change the saved gold amount.
- Work with a save code beginning with `D2S1:`.
- Generate a modified save code.
- Write the result to `new_save.txt` without overwriting the original save.

## Requirements

- Windows
- Python 3.10 or newer
- A complete D2 Survivors save code beginning with `D2S1:`

## How to Use

1. Download `editor.py.txt` from this branch.
2. Open the file in a text editor.
3. Find `SAVE_CODE` near the top of the script.
4. Replace `PASTE YOUR SAVE CODE HERE` with your complete save code, including the `D2S1:` prefix.
5. Save the file.
6. Open a terminal in the folder containing the script.
7. Run:

   ```bash
   py editor.py.txt
   ```

8. Enter the desired gold amount when prompted.
9. The script creates `new_save.txt` in the same folder.
10. Import the generated save code into the game and verify the result.

The original save is not overwritten.

## Video Tutorial

▶️ **Watch the Add Gold — No GUI tutorial:**  
https://www.youtube.com/watch?v=Mg8NvlDRU30

## Important

**Back up your original save before making changes.** This tool is provided as-is; verify the generated save in-game.

## Other Tools

- **Main repository:** https://github.com/justPLguy/D2-Survivors-Save-Editor
- **Add Gold — GUI:** https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/add-gold-gui
- **Item & Gold Editor — GUI:** https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/item-gold-editor-gui

## Credits

Created by **Just a Polish Guy**.

YouTube channel: https://www.youtube.com/@justPLguy
