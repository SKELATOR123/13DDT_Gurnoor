# Import Module
from tkinter import *
import tkinter as tk

# Root window
root = Tk()
root.geometry("1600x900")
root.title("Welcome to Assist Photography")
root.configure(bg="#000000") # colour of background

# Configure grid
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

# TITLE FRAME
frame = tk.Frame(
    root,
    bg="#515151",
    bd=3,
    relief=tk.RIDGE
)
frame.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

label = tk.Label(
    frame,
    text="Hello, Welcome to Assist Photography",
    bg="#515151",
    fg="#FFFFFF",
    font=("Arial", 50)
)
label.pack(padx=10, pady=20)

# SIDEBAR
sidebar = tk.Frame(
    root,
    bg="#515151",
    width=220,
    height=1000,
    bd=3,
    relief=tk.RIDGE
)
sidebar.grid(row=0, column=0, rowspan=2, sticky="ns")
sidebar.grid_propagate(False)

# Home button
sidebar_btn1 = tk.Button(
    sidebar,
    text="Home",
    bg="#2B2B2B",
    fg="#FFFFFF",
    font=("Arial", 14),
    width=15
)
sidebar_btn1.grid(row=0, column=0, padx=15, pady=15)

# Guides button
sidebar_btn2 = tk.Button(
    sidebar,
    text="Guides",
    bg="#2B2B2B",
    fg="#FFFFFF",
    font=("Arial", 14),
    width=15
)
sidebar_btn2.grid(row=1, column=0, padx=15, pady=15)

# Other button
sidebar_btn3 = tk.Button(
    sidebar,
    text="Other",
    bg="#2B2B2B",
    fg="#FFFFFF",
    font=("Arial", 14),
    width=15
)
sidebar_btn3.grid(row=2, column=0, padx=15, pady=15)

# CHATBOX FRAME
chatbox = tk.Frame(
    root,
    bg="#515151",
    bd=3,
    relief=tk.RIDGE
)
chatbox.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

# Chat area 
content_area = tk.Frame(
    chatbox,
    bg="#515151"
)
content_area.pack(fill="both", expand=True)

# Search bar frame at bottom
search_frame = tk.Frame(
    chatbox,
    bg="#515151"
)
search_frame.pack(fill="x", side="bottom", pady=10)

searchbar = tk.Entry(
    search_frame,
    bg="#FFFFFF",
    fg="#000000",
    font=("Arial", 14)
)
searchbar.pack(fill="x", padx=20)

# Run application
root.mainloop()

    