import base64
import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import webbrowser
import zlib

PREFIX = "D2S1:"
GITHUB_URL = "https://github.com/justPLguy/D2-Survivors-Save-Editor"
YOUTUBE_URL = "https://www.youtube.com/@justPLguy"


def decode_save(save_code):
    save_code = save_code.strip()
    if not save_code.startswith(PREFIX):
        raise ValueError("The save code must start with D2S1:")
    encoded = save_code[len(PREFIX):]
    encoded += "=" * (-len(encoded) % 4)
    raw = zlib.decompress(base64.urlsafe_b64decode(encoded))
    data = json.loads(raw.decode("utf-8"))
    if not isinstance(data, dict):
        raise ValueError("The decoded save data is not in the expected format.")
    return data


def encode_save(data):
    raw = json.dumps(data, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    encoded = base64.urlsafe_b64encode(zlib.compress(raw, level=9)).decode("ascii").rstrip("=")
    return PREFIX + encoded


class GoldEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("D2 Survivors — Gold Editor")
        self.geometry("850x700")
        self.minsize(720, 620)
        self.data = None
        self.output_code = None
        self._build_ui()

    def _build_ui(self):
        root = ttk.Frame(self, padding=16)
        root.pack(fill="both", expand=True)

        ttk.Label(
            root, text="D2 Survivors — Gold Editor",
            font=("Segoe UI", 19, "bold")
        ).pack(anchor="w")
        ttk.Label(
            root,
            text="A simple graphical tool to edit your gold — no item editing, no command line.",
            foreground="#555"
        ).pack(anchor="w", pady=(3, 14))

        save_frame = ttk.LabelFrame(root, text="1. Save code", padding=10)
        save_frame.pack(fill="both", expand=True, pady=(0, 12))
        self.save_text = tk.Text(save_frame, height=7, wrap="word", undo=True)
        self.save_text.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(save_frame, orient="vertical", command=self.save_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.save_text.configure(yscrollcommand=scrollbar.set)

        buttons = ttk.Frame(root)
        buttons.pack(fill="x", pady=(0, 12))
        ttk.Button(buttons, text="Load Save Code", command=self.load_save).pack(side="left")
        ttk.Button(buttons, text="Paste from Clipboard", command=self.paste_clipboard).pack(side="left", padx=7)
        ttk.Button(buttons, text="Clear", command=self.clear_all).pack(side="left")

        gold_frame = ttk.LabelFrame(root, text="2. Gold amount", padding=12)
        gold_frame.pack(fill="x", pady=(0, 12))
        ttk.Label(gold_frame, text="Current gold:").grid(row=0, column=0, sticky="w")
        self.current_gold_var = tk.StringVar(value="—")
        ttk.Label(
            gold_frame, textvariable=self.current_gold_var,
            font=("Segoe UI", 13, "bold"), foreground="#B8860B"
        ).grid(row=0, column=1, sticky="w", padx=(8, 20))
        ttk.Label(gold_frame, text="New gold amount:").grid(row=1, column=0, sticky="w", pady=(10, 0))
        self.gold_var = tk.StringVar()
        self.gold_entry = ttk.Entry(gold_frame, textvariable=self.gold_var, width=24)
        self.gold_entry.grid(row=1, column=1, sticky="w", padx=(8, 0), pady=(10, 0))
        ttk.Label(
            gold_frame,
            text="Enter a whole number (0 or higher).",
            foreground="#555"
        ).grid(row=2, column=1, sticky="w", padx=(8, 0), pady=(4, 0))
        gold_frame.columnconfigure(1, weight=1)

        action_row = ttk.Frame(root)
        action_row.pack(fill="x", pady=(0, 8))
        ttk.Button(
            action_row, text="Generate Modified Save",
            command=self.generate_save
        ).pack(side="left")
        ttk.Button(
            action_row, text="Save Output to File...",
            command=self.save_output
        ).pack(side="left", padx=8)
        self.status_var = tk.StringVar(value="Paste your complete save code, then click Load Save Code.")
        ttk.Label(root, textvariable=self.status_var, foreground="#555").pack(anchor="w", pady=(2, 0))

        warning = ttk.Label(
            root,
            text="Important: Back up your original save before making changes.",
            foreground="#8A5A00"
        )
        warning.pack(anchor="w", pady=(10, 0))

        footer = ttk.Frame(root)
        footer.pack(fill="x", pady=(12, 0))
        footer_left = ttk.Frame(footer)
        footer_left.pack(side="left", anchor="w")
        ttk.Label(footer_left, text="Created by Just a Polish Guy", foreground="#555").pack(side="left")
        ttk.Label(footer_left, text=" | ", foreground="#888").pack(side="left")
        self._add_link(footer_left, "GitHub", GITHUB_URL)
        ttk.Label(footer_left, text=" | ", foreground="#888").pack(side="left")
        self._add_link(footer_left, "YouTube", YOUTUBE_URL)
        ttk.Label(
            footer, text="Gold only • Simple and lightweight",
            foreground="#555"
        ).pack(side="right", anchor="e")

    def _add_link(self, parent, label, url):
        link = tk.Label(parent, text=label, fg="#0969DA", cursor="hand2",
                        font=("Segoe UI", 9, "underline"))
        link.pack(side="left")
        link.bind("<Button-1>", lambda event: webbrowser.open(url))

    def paste_clipboard(self):
        try:
            content = self.clipboard_get()
            self.save_text.delete("1.0", "end")
            self.save_text.insert("1.0", content.strip())
            self.status_var.set("Save code pasted. Click Load Save Code.")
        except tk.TclError:
            messagebox.showerror("Clipboard error", "No text could be read from the clipboard.", parent=self)

    def clear_all(self):
        self.save_text.delete("1.0", "end")
        self.data = None
        self.output_code = None
        self.current_gold_var.set("—")
        self.gold_var.set("")
        self.status_var.set("Cleared. Paste a save code to begin.")

    def load_save(self):
        code = self.save_text.get("1.0", "end").strip()
        try:
            data = decode_save(code)
            if "gold" not in data:
                raise ValueError("This save does not contain a 'gold' field.")
            gold = int(data["gold"])
            if gold < 0:
                raise ValueError("The save contains an invalid gold amount.")
        except Exception as exc:
            messagebox.showerror(
                "Could not load save",
                f"Check that you pasted the complete D2S1 save code.\n\nDetails: {exc}",
                parent=self
            )
            return
        self.data = data
        self.output_code = None
        self.current_gold_var.set(f"{gold:,}")
        self.gold_var.set(str(gold))
        self.status_var.set("Save loaded successfully. Enter the new gold amount.")

    def generate_save(self):
        if self.data is None:
            messagebox.showwarning("No save loaded", "Paste a save code and click Load Save Code first.", parent=self)
            return
        try:
            text_value = self.gold_var.get().strip()
            if not text_value:
                raise ValueError("Enter the amount of gold you want.")
            # Allow readable thousands separators without changing the stored integer.
            normalized = text_value.replace(",", "").replace(" ", "")
            gold = int(normalized)
            if gold < 0:
                raise ValueError("Gold cannot be negative.")
            self.data["gold"] = gold
            self.output_code = encode_save(self.data)
            self.status_var.set(f"Modified save generated with {gold:,} gold.")
            self.show_output(self.output_code)
        except Exception as exc:
            messagebox.showerror("Invalid gold amount", str(exc), parent=self)

    def show_output(self, output_code):
        win = tk.Toplevel(self)
        win.title("Generated Save Code")
        win.geometry("800x330")
        win.minsize(600, 250)
        ttk.Label(
            win,
            text="Copy this complete code into the game's SAVES menu:",
        ).pack(anchor="w", padx=10, pady=(10, 4))
        text = tk.Text(win, wrap="word", height=9)
        text.pack(fill="both", expand=True, padx=10, pady=4)
        text.insert("1.0", output_code)
        row = ttk.Frame(win)
        row.pack(fill="x", padx=10, pady=10)

        def copy_code():
            self.clipboard_clear()
            self.clipboard_append(output_code)
            self.update()
            messagebox.showinfo("Copied", "Save code copied to clipboard.", parent=win)

        ttk.Button(row, text="Copy Code", command=copy_code).pack(side="left")
        ttk.Button(row, text="Save to File...", command=lambda: self.save_output(output_code)).pack(side="left", padx=8)
        ttk.Button(row, text="Close", command=win.destroy).pack(side="right")

    def save_output(self, code=None):
        if code is None:
            code = self.output_code
        if not code:
            messagebox.showwarning("No output yet", "Click Generate Modified Save first.", parent=self)
            return
        path = filedialog.asksaveasfilename(
            title="Save modified save code",
            defaultextension=".txt",
            initialfile="modified_save.txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(code + "\n")
            self.status_var.set(f"Output saved to {path}")
            messagebox.showinfo("Saved", f"Modified save saved to:\n{path}", parent=self)
        except OSError as exc:
            messagebox.showerror("Save failed", str(exc), parent=self)


if __name__ == "__main__":
    app = GoldEditor()
    app.mainloop()
