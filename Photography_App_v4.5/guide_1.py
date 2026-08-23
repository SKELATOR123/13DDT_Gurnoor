import tkinter as tk


class Guide1Page(tk.Frame):
    """The Aperture guide page."""

    def __init__(self, parent, controller):
        super().__init__(parent, bg="#515151")

        # ---- Scrollable area ----
        # Wrapped everything in a Canvas + Scrollbar so if the text is ever
        # taller than the window, it scrolls instead of getting cut off
        # (this used to be a problem - the "Back to Guides" button would
        # end up pushed off the bottom of the screen).
        canvas = tk.Canvas(self, bg="#515151", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        content = tk.Frame(canvas, bg="#515151")

        content.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=content, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Lets the mouse wheel scroll the page
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # ---- Page content (goes inside "content", not "self", so it scrolls) ----
        title = tk.Label(
            content,
            text="Camera Basics",
            font=("Arial", 30),
            bg="#515151",
            fg="white"
        )

        title.pack(pady=30)

        text = tk.Label(
            content,
            text="""
This guide teaches:

• Aperture
  Aperture controls how much light enters through your lens, by
  adjusting the size of the opening (the "iris") inside it.

  It's measured in f-stops (like f/1.8, f/4, f/16). This trips a lot
  of beginners up because it's backwards from what you'd expect: a
  smaller f-number = a bigger opening = more light, and a larger
  f-number = a smaller opening = less light.

  Wide aperture (small f-number, e.g. f/1.8-f/2.8)
    - Lets in a lot of light - great for low-light shooting.
    - Produces a shallow depth of field, meaning only a thin slice of
      the image is in sharp focus while the background blurs out.
      This blur is called bokeh.
    - Popular for portraits, since it makes the subject pop against
      a soft background.

  Narrow aperture (large f-number, e.g. f/11-f/16)
    - Lets in less light.
    - Produces a deep depth of field - most or all of the scene stays
      in focus, foreground to background.
    - Popular for landscapes, where you want everything sharp.

  The trade-off: aperture is one leg of the "exposure triangle"
  (aperture, ISO, shutter speed). Opening it wider brightens the
  image but shrinks your zone of focus; closing it down keeps more
  in focus but needs more light from somewhere else.

  Quick examples:
    - Portrait with blurry background: f/1.8-f/2.8
    - Group photo, everyone in focus: f/5.6-f/8
    - Wide landscape, everything sharp: f/11-f/16

• ISO
• Shutter Speed
• Focus
• White Balance
""",
            font=("Arial", 18),
            bg="#515151",
            fg="white",
            justify="left",
            wraplength=1200  # makes long lines wrap instead of running off the screen
        )

        text.pack(padx=20)

        back = tk.Button(
            content,
            text="Back to Guides",
            command=lambda: controller.show_page("GuidesPage")
        )

        back.pack(pady=30)
