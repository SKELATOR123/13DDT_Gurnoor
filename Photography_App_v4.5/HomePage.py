import tkinter as tk
import random

# List of tips shown on the Home page. One gets picked at random each time.
TIPS = [
    "Use a wide aperture (small f-number, like f/1.8) for portraits with a blurry background.",
    "Use a narrow aperture (large f-number, like f/11-f/16) for landscapes so more of the scene stays in focus.",
    "Keep ISO as low as the lighting allows - higher ISO brightens the image but adds grainy noise.",
    "A fast shutter speed (like 1/1000s) freezes motion - great for sports or anything moving quickly.",
    "A slow shutter speed lets in more light but needs a tripod, since even slight camera shake will blur the shot.",
    "Aperture, ISO, and shutter speed all work together - this is called the exposure triangle.",
    "Golden hour (just after sunrise or before sunset) gives soft, warm, flattering light.",
    "The rule of thirds: place your subject off-center along imaginary gridlines for a more balanced photo.",
    "Clean your lens before a shoot - smudges and dust are one of the most common causes of blurry photos.",
    "Shoot in RAW format if your camera supports it - it gives you far more room to fix exposure and color later.",
]


class HomePage(tk.Frame):
    """The first page you see after logging in. Shows a welcome message and a random tip."""

    def __init__(self, parent, controller):

        super().__init__(parent, bg="#515151")
        self.controller = controller

        tk.Label(
            self,
            text="Ready to learn some photography basics?",
            font=("Arial", 30, "bold"),
            bg="#515151",
            fg="white"
        ).pack(pady=(40, 10))

        # ---- Tip of the day card ----
        tip_card = tk.Frame(
            self,
            bg="#3a3a3a",
            highlightthickness=1,
            highlightbackground="#6a6a6a"
        )
        tip_card.pack(padx=40, pady=10, fill="x")

        tk.Label(
            tip_card,
            text="Photography Tip",
            font=("Arial", 18, "bold"),
            bg="#3a3a3a",
            fg="white"
        ).pack(pady=(20, 10))

        # This label's text gets changed later by new_tip(), so I keep a
        # reference to it (self.tip_label) instead of a normal local variable
        self.tip_label = tk.Label(
            tip_card,
            text=random.choice(TIPS),
            font=("Arial", 14),
            bg="#3a3a3a",
            fg="white",
            wraplength=800,
            justify="center"
        )
        self.tip_label.pack(padx=30, pady=(0, 10))

        tk.Button(
            tip_card,
            text="New Tip",
            font=("Arial", 12),
            bg="#2B2B2B",
            fg="white",
            cursor="hand2",
            command=self.new_tip
        ).pack(pady=(0, 20))

    def new_tip(self):
        """Called when the New Tip button is clicked. Swaps in a different random tip."""
        # Build a list of every tip except the one currently showing, so
        # clicking the button always changes the tip instead of sometimes
        # picking the same one again.
        current = self.tip_label.cget("text")
        choices = [t for t in TIPS if t != current] or TIPS
        self.tip_label.config(text=random.choice(choices))
