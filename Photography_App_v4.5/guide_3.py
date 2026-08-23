import tkinter as tk


class Guide3Page(tk.Frame):
    """The Shutter Speed guide page."""

    def __init__(self, parent, controller):
        super().__init__(parent, bg="#515151")

        # ---- Scrollable area ----
        # Same Canvas + Scrollbar setup as guide_1.py and guide_2.py
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
            text="Understanding Shutter Speed",
            font=("Arial", 30),
            bg="#515151",
            fg="white"
        )

        title.pack(pady=30)

        text = tk.Label(
            content,
            text="""
Shutter speed is how long your camera's shutter stays open, exposing
the sensor to light. It's measured in seconds or fractions of a
second, like 1/1000s, 1/60s, or 2s.

• Fast shutter speed (e.g. 1/1000s)
  Freezes motion. Great for sports, wildlife, or anything moving
  quickly. Lets in less light, so you may need a wider aperture or
  higher ISO to compensate.

• Slow shutter speed (e.g. 1s or longer)
  Blurs motion and lets in more light. Used for night photography,
  light trails, or silky-smooth water shots. Almost always needs a
  tripod, since even slight camera shake will blur the whole image.

• How it fits with Aperture and ISO
  Shutter speed is one part of the "exposure triangle" along with
  Aperture and ISO. Changing one usually means adjusting another to
  keep the image properly exposed.

• Quick examples
  - Freezing sports action: 1/1000s or faster
  - Everyday handheld shots: around 1/125s
  - Light trails / night sky: several seconds, on a tripod
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
