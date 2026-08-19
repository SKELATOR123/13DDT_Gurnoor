import tkinter as tk

class HomePage(tk.Frame):

    def __init__(self,parent, controller):

        super().__init__(parent,bg="#515151")

        tk.Label(
            self,
            text="Home Page",
            font=("Arial",30),
            bg="#515151",
            fg="white"
        ).pack(pady=30)