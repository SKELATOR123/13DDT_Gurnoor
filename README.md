# Assist Photography

A app for beginner photographers. Log in, read guides on Aperture,
ISO, and Shutter Speed, get a random photography tip, and ask an AI helper
photography questions.

---

## What you need installed

- **Python 3.10 or newer**
- **Tkinter** — usually comes with Python already. If you get
  `ModuleNotFoundError: No module named 'tkinter'`, you'll need to
  reinstall Python and make sure "tcl/tk" is included in the installer
  options (on Windows it's included by default).
- **Pillow** — used to display the guide images
- **google-generativeai** — used for the AI Helper page (Gemini API)

Install the two Python packages with:

```
pip install Pillow google-generativeai
```

> If `pip install` says "Requirement already satisfied" but you still get
> `ModuleNotFoundError` when running the app, you likely have more than
> one Python installed. Use the exact Python you run the app with, e.g.:
> ```
> C:\Users\YOURNAME\AppData\Local\Programs\Python\Python312\python.exe -m pip install Pillow google-generativeai
> ```

---

## Getting a Gemini API key (for the AI Helper page)

1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
   and sign in with a Google account.
2. Click **Create API key**.
3. Set it as an environment variable so it never ends up in a shared file:
   - **Windows (PowerShell):** `setx GEMINI_API_KEY "your-key-here"`,
     then close and reopen your terminal.
   - **Mac/Linux:** add `export GEMINI_API_KEY="your-key-here"` to your
     `~/.zshrc` or `~/.bashrc`, then run `source ~/.zshrc`.
4. Alternatively, for quick local testing, you can paste the key directly
   into `config.py`. Don't share that file with the key in it.

If no key is set, the app still runs — the AI Helper page will just show
an error message when you try to ask a question.

---

## Running the app

1. Make sure your terminal is open **inside the project folder** — the
   same folder that has `main.py` and `Images/` in it. You can check this
   by running `dir` (Windows) or `ls` (Mac/Linux) — you should see
   `main.py` and `Images` listed together.
2. Run:
   ```
   python main.py
   ```
3. A login window will appear first.

> **Common error:** `FileNotFoundError: ... 'Images/...'` almost always
> means your terminal is in the wrong folder when you run the command —
> not that the file is missing. Python looks for `Images/` relative to
> wherever your terminal currently is, not relative to where `main.py`
> is saved. `cd` into the correct folder first.

---

## How to use the app

**1. Log in or register**
On first run, click **Register New Account**, enter a username and
password, then log back in with those details. You only see the main app
after a successful login.

**2. Home page**
Shows a random photography tip. Click **New Tip** for a different one.

**3. Guides page**
Click Aperture, ISO, or Shutter Speed to open that guide. Each guide page
is scrollable — use the mouse wheel or scrollbar if the text runs past
the window. Click **Back to Guides** to return.

**4. AI Helper page**
Type a photography question and press **Ask** (or hit Enter). Answers
come from Google's Gemini API, so an internet connection and a valid API
key are required.

---

## Project files

| File | What it does |
|---|---|
| `main.py` | Main app window, switches between pages |
| `login_window.py` | Login/registration window shown before the app opens |
| `database.py` | Stores user accounts (SQLite) |
| `HomePage.py` | Home page + random tip feature |
| `guides.py` | Guides menu page |
| `guide_1.py` / `guide_2.py` / `guide_3.py` | Aperture / ISO / Shutter Speed content |
| `ai_helper.py` | AI Helper chat page (Gemini API) |
| `config.py` | Where your Gemini API key goes (optional, see above) |
| `Images/` | Guide images — must stay in the same folder as `main.py` |
