## 🎥 Video Tutorial

**Watch the video to see how the D2 Survivors Gold Editor works and how to use it.**

▶️ [Watch on YouTube](https://www.youtube.com/watch?v=Mg8NvlDRU30)

## 🛠️ Download

Get the free editor and follow the setup instructions in this repository.

👉 [Download the Gold Editor](https://github.com/justPLguy/D2-Survivors-Gold-Editor/blob/main/editor.py.txt)

⚠️ Always back up your original save before making changes.

# D2 Survivors Save Editor

A simple, free Python tool for editing the **between-run gold value** in a local D2 Survivors save.

> **Unofficial community-made tool.** This project is not affiliated with or endorsed by the creators of D2 Survivors. Use it at your own risk.

## Features

- Reads a `D2S1:` save code
- Checks the save data for the `gold` field
- Lets you enter a new gold amount
- Generates a modified save code
- Saves the result as `new_save.txt` without overwriting your original save

## Requirements

- Windows
- Python 3.10 or newer
- A save code exported from D2 Survivors
- No third-party Python packages required

## Download

Download **`editor.py.txt`** from this repository.

The `.txt` extension is intentional to make the file easier to open and edit in Notepad. Python can still run it when you use the command shown below.

## How to use

1. **Back up your save first.** Export or copy your original D2 Survivors save code and keep it somewhere safe.
2. Download `editor.py.txt` from this repository.
3. Open `editor.py.txt` in Notepad.
4. Find the `SAVE_CODE` section near the top of the file:

   ```python
   SAVE_CODE = """
   PASTE YOUR SAVE CODE HERE
   """.strip()
   ```

5. Replace `PASTE YOUR SAVE CODE HERE` with your full save code, including the `D2S1:` prefix. Keep the code between the triple quotes.
6. Save the file.
7. Open the folder containing `editor.py.txt` in File Explorer.
8. Click the folder's address bar, type `cmd`, and press Enter to open Command Prompt in that folder.
9. Run:

   ```bat
   py editor.py.txt
   ```

10. Check the current gold value shown by the tool, then enter the amount you want.
11. The tool creates `new_save.txt` in the same folder.
12. Open `new_save.txt`, copy the complete generated save code, and import it into the game using the game's save import feature, if available.

## Important notes

- This tool edits the `gold` field in the saved data. It does **not** currently edit gold during an active run.
- Always keep an untouched backup of your original save.
- The game may reject a modified save if its format or validation rules change. Test carefully and never overwrite your only backup.
- Do not publish your personal save code. It may contain progress or other data you want to keep private.

## Troubleshooting

### `Invalid save-code prefix`
Make sure the save code starts with `D2S1:` and that you pasted the entire code.

### Error while decoding or decompressing
Check that the save code is complete and has no missing characters. Export a fresh save from the game and try again.

### `Could not find the 'gold' field`
The save format may have changed. Do not import output generated from an incompatible save.

### `py` is not recognized
Install Python for Windows from the official website: https://www.python.org/downloads/windows/

## How it works

The script decodes the URL-safe Base64 payload, decompresses it with zlib, parses the JSON data, updates `gold`, then compresses and encodes the data again.

## Credits

Made by a community member for educational and personal-use purposes.
