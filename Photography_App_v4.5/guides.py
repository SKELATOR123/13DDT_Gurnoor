import tkinter as tk
from guide_1 import Guide1Page
from PIL import Image, ImageTk

# Background colour used for every guide "card" - kept as one variable so
# all three cards always match if I want to change the colour later
CARD_BG = "#3a3a3a"


class GuidesPage(tk.Frame):
    """Shows all the guides (Aperture, ISO, Shutter Speed) as clickable image cards."""

    def __init__(self, parent, controller):

        super().__init__(parent, bg="#515151")
        self.controller = controller

        # ---- Scrollable, centered area ----
        # I'm using a Canvas + Scrollbar here so the page can scroll if the
        # cards don't all fit on screen (e.g. if I add more guides later).
        canvas = tk.Canvas(self, bg="#515151", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        content = tk.Frame(canvas, bg="#515151")

        window_id = canvas.create_window((0, 0), window=content, anchor="n")

        def _on_content_configure(event):
            # Updates the scrollable area whenever the content changes size
            canvas.configure(scrollregion=canvas.bbox("all"))

        def _on_canvas_configure(event):
            # Makes "content" match the canvas's width so it can be centered
            # properly, instead of just being as wide as the cards inside it
            canvas.itemconfig(window_id, width=event.width)
            # Re-centers the content horizontally whenever the window is resized
            canvas.coords(window_id, event.width / 2, 0)

        content.bind("<Configure>", _on_content_configure)
        canvas.bind("<Configure>", _on_canvas_configure)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def _on_mousewheel(event):
            # Lets the mouse wheel scroll the page
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # ---- Page content ----
        tk.Label(
            content,
            text="Photography Guides",
            font=("Arial", 30, "bold"),
            bg="#515151",
            fg="white"
        ).pack(pady=(30, 10))

        tk.Label(
            content,
            text="Pick a topic to learn the basics.",
            font=("Arial", 14),
            bg="#515151",
            fg="#cccccc"
        ).pack(pady=(0, 30))

        # Frame that arranges the guide cards in a grid: 2 per row
        grid = tk.Frame(content, bg="#515151")
        grid.pack()

        # Aperture card (top left)
        self._make_card(
            grid, row=0, column=0,
            image_path="Images/Aperture_Guide_Image.png",
            page_name="Guide1Page",
            caption="Learn how aperture controls light and creates background blur."
        )

        # ISO card (top right)
        self._make_card(
            grid, row=0, column=1,
            image_path="Images/ISO_Guide_Image.jpeg",
            page_name="Guide2Page",
            caption="Learn how ISO affects brightness and image quality."
        )

        # Shutter Speed card (spans both columns so it sits centered on its own row)
        self._make_card(
            grid, row=1, column=0, columnspan=2,
            image_path="Images/ShutterSpeed_Guide_Image.jpeg",
            page_name="Guide3Page",
            caption="Learn how shutter speed freezes or blurs motion."
        )

    def _make_card(self, parent, row, column, image_path, page_name, caption, columnspan=1):
        """Builds one guide card: a bordered box with a clickable image and a caption below it."""

        card = tk.Frame(
            parent,
            bg=CARD_BG,
            bd=0,
            highlightthickness=1,
            highlightbackground="#6a6a6a"
        )
        card.grid(row=row, column=column, columnspan=columnspan, padx=20, pady=20)

        img = ImageTk.PhotoImage(Image.open(image_path).resize((220, 220)))
        # Tkinter forgets about images that aren't stored somewhere, so I save
        # it as an attribute on self here or it would disappear off the button
        setattr(self, f"_img_{page_name}", img)

        button = tk.Button(
            card,
            image=img,
            bd=0,
            highlightthickness=0,
            cursor="hand2",
            command=lambda: self.controller.show_page(page_name)
        )
        button.pack(padx=15, pady=(15, 10))

        tk.Label(
            card,
            text=caption,
            bg=CARD_BG,
            fg="white",
            font=("Arial", 13),
            wraplength=220,
            justify="center"
        ).pack(padx=15, pady=(0, 15))
