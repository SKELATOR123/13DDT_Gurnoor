import tkinter as tk


class Guide2Page(tk.Frame):
    """The ISO guide page."""

    def __init__(self, parent, controller):
        super().__init__(parent, bg="#515151")

        # ---- Scrollable area ----
        # Same Canvas + Scrollbar setup as guide_1.py, so the page scrolls
        # instead of the text/back button getting cut off the window
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

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # ---- Page content ----
        title = tk.Label(
            content,
            text="Understanding ISO",
            font=("Arial", 30),
            bg="#515151",
            fg="white"
        )

        title.pack(pady=30)

        text = tk.Label(
            content,
            text="""
ISO controls how sensitive your camera's sensor is to light.

• Low ISO (100-200)
  Less sensitive to light. Produces clean, sharp images with very
  little grain. Best used in bright conditions, like outdoors on a
  sunny day.

• High ISO (800 and above)
  More sensitive to light. Lets you shoot in darker conditions
  without a flash or tripod, but introduces "noise" - a grainy,
  speckled look, especially in shadows.

• The trade-off
  Raising ISO brightens your image, but at the cost of quality.
  The general rule is: use the lowest ISO you can get away with
  for the lighting you're in, and only raise it when you need to.

• Quick examples
  - Sunny day outdoors: ISO 100-200
  - Indoors / overcast: ISO 400-800
  - Night / low light: ISO 1600+
""",
            font=("Arial", 18),
            bg="#515151",
            fg="white",
            justify="left",
            wraplength=1200
        )

        text.pack(padx=20)

        back = tk.Button(
            content,
            text="Back to Guides",
            command=lambda: controller.show_page("GuidesPage")
        )

        back.pack(pady=30)
