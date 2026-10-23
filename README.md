::: {align="center"}
# ⚔️ D2 Survivors Save Editor

### An advanced community-made save editor for **D2 Survivors**

Edit gold, character skills, equipment modifiers, inventory items, and
mercenary gear --- with a preview of your changes before exporting your
modified save.

[**⬇️ Download the latest version from
Releases**](https://github.com/justPLguy/D2-Survivors-Save-Editor/releases)
:::

------------------------------------------------------------------------

## ✨ Overview

**D2 Survivors Save Editor** is a standalone save-editing tool created
by **Just a Polish Guy** for players who want more control over their
*D2 Survivors* save data.

The editor reads the game's `D2S1` save code, decodes its data, lets you
make selected changes through a graphical interface, and generates an
updated save code that you can use in the game.

The project is community-made and is not affiliated with or endorsed by
the game's developers.

## 🧰 Features

### 💰 Gold editing

-   View and change the shared gold value stored in the save.
-   Apply the new value explicitly with **Apply Gold**.
-   Validate the entered value and confirm the change before it is
    included in the output.
-   Review the gold change in the change preview.

### 🧙 Character and skill editing

-   Select a character class and inspect the skills available in the
    loaded save.
-   Edit supported active and passive skill levels.
-   Stage skill changes before applying them, so you can review the
    planned edits first.
-   See which skills are present in the save and which are unavailable
    for that character.
-   Use the skill catalog's supported maximum levels to validate edits.
-   Keep passive skill data synchronized with the save's related history
    markers.
-   Undo the most recently applied batch of skill changes.
-   Switch between character classes without losing staged edits.

**Important:** Skills that are not present in the loaded save are
treated as unavailable. The editor does not add missing skills to a
save.

### 🛡️ Equipment and item modifiers

-   Browse supported equipped items for the character.
-   Inspect inventory items and edit supported numeric modifiers.
-   Browse the assigned mercenary and its equipment separately.
-   Edit supported modifiers on character equipment, inventory items,
    and mercenary equipment.
-   Keep pending modifier edits when switching between items.
-   Use clear item-and-modifier labels to identify what you are editing.

The modifiers available for editing depend on the item data and the
properties supported by the editor.

### 🔍 Change preview

Review your pending changes before exporting the save.

The preview can show changes by category: - **Skills** --- skill and
passive level changes. - **Items** --- supported item modifier
changes. - **Gold** --- the gold value change. - **Other** --- other
detected changes, when applicable.

The preview includes category counts and a total change count. Rows are
color-coded to make increases, decreases, and other types of changes
easier to distinguish.

The editor filters out noisy internal history-array differences so the
preview focuses on changes made by the user rather than incidental data
reordering.

### ↩️ Reset, undo, and backup

-   **Reset Changes** clears pending edits so you can start again from
    the loaded save.
-   **Undo** restores the previous applied batch of skill changes.
-   Create a backup of the original save data before making changes.

These safeguards help you review and recover from editing mistakes. They
are not a substitute for keeping your own copy of the original save.

### 📂 Loading and exporting saves

-   Load a save by entering its `D2S1` save code.
-   Load save data from a file using the startup loader.
-   Decode the save for editing in the graphical interface.
-   Generate a modified `D2S1` save code after reviewing and confirming
    your changes.
-   Save the resulting code to a text file.

The editor is designed to preserve the save's underlying data structure
while making supported edits.

## 🧭 How to use the editor

1.  **Get the editor** from the project's [Releases
    page](https://github.com/justPLguy/D2-Survivors-Save-Editor/releases).
2.  **Load your save** by entering the save code or selecting a file in
    the startup loader.
3.  **Choose what to edit** --- gold, character skills, equipped items,
    inventory items, or mercenary equipment.
4.  **Apply and review edits.** Confirm gold changes with **Apply
    Gold**, and stage skill changes before applying them.
5.  **Open the change preview** and check the categories, values, and
    total change count.
6.  **Export the modified save code** and save it to a text file if
    desired.
7.  **Keep your original save untouched** until you have confirmed that
    the modified save works as expected in the game.

Exact interface labels may vary between versions. Check the release
notes for the version you are using.

## ⚠️ Important notes

-   **Always back up your original save before editing.**
-   This is an unofficial, community-made tool. Use it at your own
    discretion.
-   Only the features and modifiers supported by the current editor can
    be edited.
-   Skills absent from a loaded save cannot be added through the skill
    editor.
-   In-game testing has primarily focused on the Necromancer
    skill-editing workflow. Other classes and individual modifiers may
    require additional testing.
-   If a modified save does not behave as expected, restore your backup.

## 📥 Download

The latest published builds and version-specific release information are
available here:

### [➡️ D2 Survivors Save Editor --- Releases](https://github.com/justPLguy/D2-Survivors-Save-Editor/releases)

Download the version listed on the Releases page. The repository's
source code and the downloadable release builds may be provided
separately.

## 🗺️ Project

-   **Repository:** [D2 Survivors Save
    Editor](https://github.com/justPLguy/D2-Survivors-Save-Editor)
-   **Developer profile:** [Just a Polish Guy on
    GitHub](https://github.com/justPLguy)

## ❤️ Credits

Created by **Just a Polish Guy**.

-   **Facebook:**
    [facebook.com/justPLguy](https://www.facebook.com/justPLguy)
-   **YouTube:**
    [youtube.com/@justPLguy](https://www.youtube.com/@justPLguy)
-   **GitHub:** [github.com/justPLguy](https://github.com/justPLguy)

If you find the tool useful, consider following the project and checking
back for updates.

------------------------------------------------------------------------

::: {align="center"}
**D2 Survivors Save Editor** · Community-made tool · Not affiliated with
the game's developers
:::
