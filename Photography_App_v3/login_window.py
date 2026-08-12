import tkinter as tk
from tkinter import messagebox
import database


class LoginWindow(tk.Tk):
    """Standalone login window, shown before the main app."""

    def __init__(self):
        super().__init__()
        self.logged_in = False

        self.title("Login - Assist Photography")
        self.geometry("400x400")
        self.configure(bg="#515151")
        self.resizable(False, False)

        # Title
        tk.Label(self, text="Account Login", font=("Arial", 24), bg="#515151", fg="white").pack(pady=30)

        # Username Input
        tk.Label(self, text="Username:", font=("Arial", 14), bg="#515151", fg="white").pack(pady=5)
        self.username_entry = tk.Entry(self, font=("Arial", 14), width=25)
        self.username_entry.pack(pady=5)

        # Password Input
        tk.Label(self, text="Password:", font=("Arial", 14), bg="#515151", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self, font=("Arial", 14), width=25, show="*")
        self.password_entry.pack(pady=5)
        self.password_entry.bind("<Return>", lambda event: self.handle_login())

        # Action Buttons
        tk.Button(self, text="Login", font=("Arial", 12), width=10, bg="#2B2B2B", fg="white", command=self.handle_login).pack(pady=15)

        tk.Button(self, text="Register New Account", font=("Arial", 10), bg="#515151", fg="lightblue", bd=0, command=self.handle_register).pack(pady=5)

    def handle_login(self):
            username = self.username_entry.get().strip()
            password = self.password_entry.get().strip()

            if database.login_user(username, password):
                self.logged_in = True
                self.destroy()  # Close the login window
            else:
                messagebox.showerror("Error", "Invalid username or password.")

    def handle_register(self):
            username = self.username_entry.get().strip()
            password = self.password_entry.get().strip()

            success, message = database.register_user(username, password)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)






