import tkinter as tk
from guide_1 import Guide1Page

class GuidesPage(tk.Frame):

    def __init__(self,parent, controller):

        super().__init__(parent,bg="#515151")
        self.controller = controller 


        tk.Label(
            self,
            text="Photography Guides",
            font=("Arial",30),
            bg="#515151",
            fg="white"
        ).pack(pady=20)

        # First Guide
        guide1 = tk.Button(
            self,
            text="IMAGE",
            width=20,
            height=10,
            font=("Arial",20),
            command=lambda: self.controller.show_page("Guide1Page") 
        )

        guide1.pack(pady=20)

        tk.Label(
            self,
            text="Learn the basics of your camera.",
            bg="#515151",
            fg="white",
            font=("Arial",14)
        ).pack()