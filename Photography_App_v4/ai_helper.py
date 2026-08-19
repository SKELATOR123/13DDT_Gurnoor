import tkinter as tk
import threading
import os
import google.generativeai as genai

try:
    from config import GEMINI_API_KEY as CONFIG_KEY
except ImportError:
    CONFIG_KEY = None

# Prefer an environment variable (safer — never ends up in a shared file).
# Fall back to config.py for convenience during local development.
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or CONFIG_KEY

SYSTEM_PROMPT = (
    "You are a friendly photography tutor helping complete beginners. "
    "Explain concepts simply, avoid unexplained jargon, and keep answers "
    "short and practical."
)


class AIHelperPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg="#515151")
        self.controller = controller

        # Set up the Gemini model once. If the key hasn't been filled in,
        # we still build the page, we just show an error when they try to ask.
        self.model = None
        self.setup_error = None
        try:
            if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_API_KEY_HERE":
                self.setup_error = (
                    "No API key set. Open config.py and paste your Gemini "
                    "API key into GEMINI_API_KEY."
                )
            else:
                genai.configure(api_key=GEMINI_API_KEY)
                self.model = genai.GenerativeModel("gemini-flash-latest")
        except Exception as e:
            self.setup_error = f"Could not set up Gemini: {e}"

        tk.Label(
            self,
            text="AI Photography Helper",
            font=("Arial", 30),
            bg="#515151",
            fg="white"
        ).pack(pady=20)

        tk.Label(
            self,
            text="Ask a question about photography and get an AI-generated answer.",
            font=("Arial", 14),
            bg="#515151",
            fg="white"
        ).pack(pady=(0, 10))

        # Conversation display (read-only)
        self.conversation = tk.Text(
            self,
            width=90,
            height=20,
            font=("Arial", 12),
            bg="#2B2B2B",
            fg="white",
            wrap="word",
            state="disabled"
        )
        self.conversation.pack(padx=20, pady=10, fill="both", expand=True)

        # Input row
        input_row = tk.Frame(self, bg="#515151")
        input_row.pack(fill="x", padx=20, pady=(0, 20))

        self.question_entry = tk.Entry(input_row, font=("Arial", 14))
        self.question_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.question_entry.bind("<Return>", lambda event: self.on_ask())

        self.ask_button = tk.Button(
            input_row,
            text="Ask",
            font=("Arial", 12),
            bg="#2B2B2B",
            fg="white",
            command=self.on_ask
        )
        self.ask_button.pack(side="left")

    def append_to_conversation(self, speaker, text):
        self.conversation.config(state="normal")
        self.conversation.insert("end", f"{speaker}: {text}\n\n")
        self.conversation.config(state="disabled")
        self.conversation.see("end")

    def on_ask(self):
        question = self.question_entry.get().strip()
        if not question:
            return

        if self.setup_error:
            self.append_to_conversation("Error", self.setup_error)
            return

        self.question_entry.delete(0, "end")
        self.append_to_conversation("You", question)
        self.ask_button.config(state="disabled")

        threading.Thread(target=self._get_answer, args=(question,), daemon=True).start()

    def _get_answer(self, question):
        try:
            response = self.model.generate_content(SYSTEM_PROMPT + "\n\nQuestion: " + question)
            answer = response.text
        except Exception as e:
            answer = f"Something went wrong talking to Gemini: {e}"

        # Hand the UI update back to the main thread
        self.after(0, lambda: self._show_answer(answer))

    def _show_answer(self, answer):
        self.append_to_conversation("AI", answer)
        self.ask_button.config(state="normal")
