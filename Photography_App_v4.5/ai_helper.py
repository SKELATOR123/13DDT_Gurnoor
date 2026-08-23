import tkinter as tk
import threading
import os
import google.generativeai as genai

try:
    from config import GEMINI_API_KEY as CONFIG_KEY
except ImportError:
    CONFIG_KEY = None

# I check for an environment variable first (safer - the key never ends up
# in a file that could get shared/uploaded), and fall back to config.py
# so it's still easy to test locally.
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or CONFIG_KEY

# This gets sent along with every question so the AI answers like a
# photography tutor instead of just a generic chatbot
SYSTEM_PROMPT = (
    "You are a friendly photography tutor helping complete beginners. "
    "Explain concepts simply, avoid unexplained jargon, and keep answers "
    "short and practical."
)


class AIHelperPage(tk.Frame):
    """A chat-style page where you can ask the AI a photography question."""

    def __init__(self, parent, controller):
        super().__init__(parent, bg="#515151")
        self.controller = controller

        # Set up the Gemini model once when the page is created. If there's
        # no API key yet, I don't crash the whole app - I just remember the
        # error and show it later if someone actually tries to ask a question.
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

        # This box shows the whole conversation. state="disabled" makes it
        # read-only so the user can't type directly into it.
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

        # A "tag" lets me colour just the AI's replies differently to "You"/"Error"
        self.conversation.tag_config("ai", foreground="#51ff4b")

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
        """Adds one line to the conversation box, e.g. append_to_conversation("You", "hi")."""
        self.conversation.config(state="normal")  # unlock it so I can add text
        tag = "ai" if speaker == "AI" else ()
        self.conversation.insert("end", f"{speaker}: {text}\n\n", tag)
        self.conversation.config(state="disabled")  # lock it again
        self.conversation.see("end")  # scroll down to show the newest message

    def on_ask(self):
        """Runs when the Ask button is clicked (or Enter is pressed)."""
        question = self.question_entry.get().strip()
        if not question:
            return  # don't bother sending an empty question

        if self.setup_error:
            self.append_to_conversation("Error", self.setup_error)
            return

        self.question_entry.delete(0, "end")
        self.append_to_conversation("You", question)
        self.ask_button.config(state="disabled")  # stops spamming the button while waiting

        # Talking to the API takes a second or two. If I did this on the main
        # thread, the whole app would freeze while waiting. Running it on a
        # separate thread keeps the app responsive.
        threading.Thread(target=self._get_answer, args=(question,), daemon=True).start()

    def _get_answer(self, question):
        """Runs on the background thread - actually calls the Gemini API."""
        try:
            response = self.model.generate_content(SYSTEM_PROMPT + "\n\nQuestion: " + question)
            answer = response.text
        except Exception as e:
            answer = f"Something went wrong talking to Gemini: {e}"

        # Tkinter isn't safe to update from a background thread, so I use
        # self.after() to hand the result back to the main thread
        self.after(0, lambda: self._show_answer(answer))

    def _show_answer(self, answer):
        """Runs back on the main thread once the AI's answer is ready."""
        self.append_to_conversation("AI", answer)
        self.ask_button.config(state="normal")  # let the user ask another question
