import tkinter as tk

# All the different pages/screens of the app
from HomePage import HomePage
from guides import GuidesPage
from guide_1 import Guide1Page 
from guide_2 import Guide2Page
from guide_3 import Guide3Page
from login_window import LoginWindow
from ai_helper import AIHelperPage


class App(tk.Tk):
    """This is the main app window. It holds the sidebar and swaps between pages."""

    def __init__(self):
        super().__init__()

        # ---------------- Window ----------------
        self.title("Assist Photography")
        self.geometry("1600x900")
        self.configure(bg="black")
        self.iconbitmap("Images/app_icon.ico")

        # Makes the content area (column 1, row 1) grow when the window is resized
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ---------------- Sidebar ----------------
        sidebar = tk.Frame(
            self,
            bg="#515151",
            width=220,
            bd=3,
            relief="ridge"
        )

        sidebar.grid(row=0, column=0, rowspan=2, sticky="ns")
        # Stops the sidebar from shrinking to fit whatever buttons are inside it
        sidebar.grid_propagate(False)

        # ---------------- Header ----------------
        header = tk.Frame(
            self,
            bg="#515151",
            bd=3,
            relief="ridge"
        )

        header.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        title = tk.Label(
            header,
            text="Hello, Welcome to Assist Photography",
            font=("Arial", 32),
            bg="#515151",
            fg="white"
        )

        title.pack(pady=20)

        # ---------------- Main Content ----------------
        # This frame is where every page (Home, Guides, AI Helper, etc.) gets placed
        self.container = tk.Frame(
            self,
            bg="#515151",
            bd=3,
            relief="ridge"
        )

        self.container.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Keeps track of every page so I can look it up by name later
        self.pages = {}

        # Build every page once and stack them on top of each other in the same spot.
        # show_page() then just brings the right one to the front.
        for Page in (HomePage, GuidesPage, Guide1Page, Guide2Page, Guide3Page, AIHelperPage):

            page = Page(self.container, self)

            self.pages[Page.__name__] = page

            page.grid(row=0, column=0, sticky="nsew")

        # ---------------- Sidebar Buttons ----------------
        tk.Button(
            sidebar,
            text="Home",
            font=("Arial", 14),
            width=15,
            bg="#2B2B2B",
            fg="white",
            command=lambda: self.show_page("HomePage")
        ).grid(row=0, column=0, padx=15, pady=15)

        tk.Button(
            sidebar,
            text="Guides",
            font=("Arial", 14),
            width=15,
            bg="#2B2B2B",
            fg="white",
            command=lambda: self.show_page("GuidesPage")
        ).grid(row=1, column=0, padx=15, pady=15)

        tk.Button(
            sidebar,
            text="AI Helper",
            font=("Arial", 14),
            width=15,
            bg="#2B2B2B",
            fg="white",
            command=lambda: self.show_page("AIHelperPage")
        ).grid(row=2, column=0, padx=15, pady=15)

        # Home is the first thing you see once the app opens
        self.show_page("HomePage")

    def show_page(self, page_name):
        """Brings whichever page is passed in to the front, hiding the others."""
        self.pages[page_name].tkraise()


if __name__ == "__main__":
    # Show the login window first. This pauses here (mainloop) until the
    # login window is closed - either by logging in, or the user just closing it.
    login_window = LoginWindow()
    login_window.mainloop()

    # Only open the main app if the login actually succeeded.
    # This is what stops someone from skipping the login screen.
    if login_window.logged_in:
        app = App()
        app.mainloop()
