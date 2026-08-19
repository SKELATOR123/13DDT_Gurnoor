import tkinter as tk
from guide_1 import Guide1Page
from PIL import Image, ImageTk

class GuidesPage(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent, bg="#515151")
        self.controller = controller

        tk.Label(
            self,
            text="Photography Guides",
            font=("Arial", 30),
            bg="#515151",
            fg="white"
        ).pack(pady=20)

        # First Guide
        self.guide1_img = ImageTk.PhotoImage(
            Image.open("images/Aperture_Guide_Image.png").resize((200, 200))
        )

        guide1 = tk.Button(
            self,
            image=self.guide1_img,
            command=lambda: self.controller.show_page("Guide1Page")
        )

        guide1.pack(pady=20)

        tk.Label(
            self,
            text="Learn the basics of your camera.",
            bg="#515151",
            fg="white",
            font=("Arial", 14)
        ).pack()