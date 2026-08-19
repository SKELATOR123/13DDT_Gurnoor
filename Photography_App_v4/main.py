import tkinter as tk

# Import the pages
from HomePage import HomePage
from guides import GuidesPage
from guide_1 import Guide1Page
from login_window import LoginWindow
from ai_helper import AIHelperPage


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # ---------------- Window ----------------
        self.title("Assist Photography")
        self.geometry("1600x900")
        self.configure(bg="black")

        # Allow the content area to resize
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

        # Dictionary storing all pages
        self.pages = {}

        # Create pages
        for Page in (HomePage, GuidesPage, Guide1Page, AIHelperPage):

            page = Page(self.container,self)

            self.pages[Page.__name__] = page

            page.grid(row=0, column=0, sticky="nsew")

        # Sidebar Buttons
        tk.Button(
            sidebar,
            text="Home",
            font=("Arial",14),
            width=15,
            bg="#2B2B2B",
            fg="white",
            command=lambda:self.show_page("HomePage")
        ).grid(row=0,column=0,padx=15,pady=15)

        tk.Button(
            sidebar,
            text="Guides",
            font=("Arial",14),
            width=15,
            bg="#2B2B2B",
            fg="white",
            command=lambda:self.show_page("GuidesPage")
        ).grid(row=1,column=0,padx=15,pady=15)

        tk.Button(
            sidebar,
            text="AI Helper",
            font=("Arial",14),
            width=15,
            bg="#2B2B2B",
            fg="white",
            command=lambda:self.show_page("AIHelperPage")
        ).grid(row=2,column=0,padx=15,pady=15)

        # Show Home first
        self.show_page("HomePage")

    # Bring a page to the front
    def show_page(self,page_name):
        self.pages[page_name].tkraise()

if __name__ == "__main__":
    # Show the login window first
    login_window = LoginWindow()
    login_window.mainloop()

    # If login was successful, show the main app
    if login_window.logged_in:
        app = App()
        app.mainloop()