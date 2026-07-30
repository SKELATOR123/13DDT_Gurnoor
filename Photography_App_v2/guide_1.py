import tkinter as tk


class Guide1Page(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg="#515151")

        title = tk.Label(
            self,
            text="Camera Basics",
            font=("Arial",30),
            bg="#515151",
            fg="white"
        )

        title.pack(pady=30)

        text = tk.Label(
            self,
            text="""
This guide teaches:

• Aperture
• ISO
• Shutter Speed
• Focus
• White Balance
""",
            font=("Arial",18),
            bg="#515151",
            fg="white",
            justify="left"
        )

        text.pack()

        back = tk.Button(
            self,
            text="Back to Guides",
            command=lambda: controller.show_page("GuidesPage")
        )

        back.pack(pady=30)