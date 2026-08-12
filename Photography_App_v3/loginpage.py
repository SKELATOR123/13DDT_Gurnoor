import tkinter as tk
from tkinter import messagebox
import database

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#515151")
        self.controller = controller

        # Title
        tk.Label(self, text="Account Login", font=("Arial", 30), bg="#515151", fg="white").pack(pady=40)

        # Username Input
        tk.Label(self, text="Username:", font=("Arial", 14), bg="#515151", fg="white").pack(pady=5)
        self.username_entry = tk.Entry(self, font=("Arial", 14), width=25)
        self.username_entry.pack(pady=5)

        # Password Input
        tk.Label(self, text="Password:", font=("Arial", 14), bg="#515151", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self, font=("Arial", 14), width=25, show="*")
        self.password_entry.pack(pady=5)

        # Action Buttons
        tk.Button(self, text="Login", font=("Arial", 12), width=10, bg="#2B2B2B", fg="white", command=self.handle_login).pack(pady=15)
        tk.Button(self, text="Register New Account", font=("Arial", 10), bg="#515151", fg="lightblue", bd=0, command=self.handle_register).pack(pady=5)

    def handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if database.login_user(username, password):
            messagebox.showinfo("Success", f"Welcome back, {username}!")
            self.controller.show_page("HomePage")
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