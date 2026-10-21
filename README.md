# D2 Survivors Save Editor

A collection of community-made tools for editing save data in **D2 Survivors**.

The project currently focuses on two versions of the editor: a lightweight command-line tool for changing gold and a graphical interface for editing gold and equipped item modifiers across different character classes.

> **Disclaimer:** This is an unofficial community project. It is not affiliated with or endorsed by the creators of D2 Survivors or Blizzard Entertainment. Use at your own risk and always back up your original save.

## 🛠️ Available Tools

### 1. Add Gold — No GUI / 
LINK - https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/add-gold-no-gui

**Branch:** `add-gold-no-gui`

A simple Python tool for players who want to change their saved gold without using a graphical interface.

Features:
- Edit the saved gold value.
- Process a `D2S1:` save code.
- Generate a modified save code.
- Save the result to a separate file without overwriting the original.

**Best for:** Players who want a lightweight, straightforward tool.

### 2. Item & Gold Editor — GUI
LINK - [https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/add-gold-no-gui](https://github.com/justPLguy/D2-Survivors-Save-Editor/tree/item-gold-editor-gui)

**Branch:** `item-gold-editor-gui`

A graphical save editor with equipment management for different character classes.

Features:
- Graphical Windows interface.
- Separate equipment lists for each character class.
- View equipped items and their modifiers.
- Edit item stats such as Life, Mana, Strength and resistances when supported by the save data.
- Change saved gold.
- Preserve edits when switching between items and classes.
- Generate and copy the modified save code.
- Export the result to a text file.

**Best for:** Players who want to edit equipment and character-related item modifiers through a graphical interface.

## 💻 Requirements

- Windows
- Python 3.10 or newer
- A D2 Survivors save code beginning with `D2S1:`

The GUI version uses Python's built-in Tkinter library and does not require additional Python packages in a standard installation that includes Tkinter.

## 🚀 Getting Started

1. Choose the editor that fits your needs.
2. Open its branch in this repository.
3. Download the relevant Python script.
4. Follow the instructions provided for that version.
5. Export your save from the game, make your changes and import the generated save back into the game.

## ⚠️ Important

- Always make a backup of your original save before editing.
- Verify the modified save in-game before replacing your backup.
- Available modifiers depend on the data stored in the save file.
- This project is provided as-is, without guarantees.

## 📌 Project Roadmap

- [x] Edit saved gold.
- [x] Edit equipped item modifiers.
- [x] Separate equipment views for character classes.
- [x] Graphical user interface.
- [ ] Add graphical item previews to the GUI.
- [ ] Improve documentation and ease of use.

## 👤 Author

Created by **Just a Polish Guy**.

- GitHub: https://github.com/justPLguy
- YouTube: https://www.youtube.com/watch?v=Mg8NvlDRU30

If you find this project useful, consider starring the repository ⭐
