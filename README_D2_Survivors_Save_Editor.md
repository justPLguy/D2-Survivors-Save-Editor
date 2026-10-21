# D2 Survivors Save Editor

A small Python tool for editing the **between-run gold value** in a local D2 Survivors save.

> **Disclaimer:** This is an unofficial, community-made tool and is not affiliated with or endorsed by the creators of D2 Survivors. Use it at your own risk.

## Features

- Reads a `D2S1:` save code
- Decodes the save data and checks for the `gold` field
- Lets you enter a new gold amount
- Re-encodes the modified save
- Writes the result to `new_save.txt` without overwriting your original save

## Requirements

- Windows
- Python 3.10 or newer
- A save code exported from D2 Survivors

No third-party Python packages are required.

## How to use

1. **Back up your save first.** Export or copy your original D2 Survivors save code and keep it somewhere safe.
2. Download `editor.py` from this repository.
3. Open `editor.py` in a text editor.
4. Replace `PASTE YOUR SAVE CODE HERE` inside `SAVE_CODE` with your full save code, including the `D2S1:` prefix. Keep the code inside the triple quotes.
5. Save the file.
6. Open Command Prompt in the folder containing `editor.py`.
7. Run:

   ```bat
   py editor.py
   ```

8. Check the current gold value shown by the tool, then enter the amount you want.
9. The tool creates `new_save.txt` in the same folder.
10. Copy the complete generated code from `new_save.txt` and use the game's save import feature, if available.

## Important notes

- This tool edits the `gold` field in the save data. It does **not** currently edit gold earned during an active run.
- Always keep an untouched backup of your original save.
- The game may reject a modified save if its format or validation rules change. Test carefully and do not overwrite your only backup.
- Never share a save code publicly if it contains progress or other data you want to keep private.

## Troubleshooting

### `Invalid save-code prefix`
Make sure the save code starts with `D2S1:` and that you pasted the entire code.

### `Error` while decoding or decompressing
Check that the save code is complete and has no extra spaces or missing characters. Export a fresh save from the game and try again.

### `Could not find the 'gold' field`
The save format may have changed. Do not import an output generated from an incompatible save.

## How it works

The script decodes the URL-safe Base64 payload, decompresses it with zlib, parses the JSON data, updates `gold`, and then compresses and encodes the data again.

## Credits

Made by a community member for educational and personal-use purposes.
