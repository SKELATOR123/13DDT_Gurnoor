# Import Module
from tkinter import *
import tkinter as tk

#root window title and dimension
root = Tk()
root.geometry('3440x1440')
root.title("Welcome to Assist Photography")
root['bg'] = "#000000"

#Creating a Title frame
frame = tk.Frame(root, bg="#515151", width=200, height=100, bd=3, relief=tk.RIDGE)
frame.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

label = tk.Label(frame, text="Hello, Welcome to Assist Photography", bg="#515151", fg="#FFFFFF", font=("Arial", 50))
label.grid(pady=20)

#creating a sidebar frame
sidebar = tk.Frame(root, bg="#515151", width=200, height=1000, bd=3, relief=tk.RIDGE)
sidebar.grid(row=0, column=0, rowspan=2)

# Stop the sidebar from shrinking to fit the button size
sidebar.grid_propagate(False)

# Add a button inside the sidebar using grid
sidebar_btn1 = tk.Button(
    sidebar, 
    text="Home", 
    bg="#2B2B2B", 
    fg="#FFFFFF", 
    font=("Arial", 14),
    width=15
)
sidebar_btn1.grid(row=0, column=0, padx=15, pady=15)

# Add a button inside the sidebar using grid
sidebar_btn2 = tk.Button(
    sidebar, 
    text="Gides", 
    bg="#2B2B2B", 
    fg="#FFFFFF", 
    font=("Arial", 14),
    width=15
)
sidebar_btn2.grid(row=1, column=0, padx=15, pady=15)

# Add a button inside the sidebar using grid
sidebar_btn3 = tk.Button(
    sidebar, 
    text="Other", 
    bg="#2B2B2B", 
    fg="#FFFFFF", 
    font=("Arial", 14),
    width=15
)
sidebar_btn3.grid(row=2, column=0, padx=15, pady=15)

chatbox= tk.Frame(root, bg="#515151", width=1300, height=1000, bd=3, relief=tk.RIDGE)
chatbox.grid(row=1, column=1, columnspan=5, rowspan=10, padx=10, pady=10)

searchbar = tk.Entry(chatbox, bg="#FFFFFF", fg="#000000", font=("Arial", 14), width=50)
searchbar.grid(row=0, column=0, padx=10, pady=10)


#all widgets will go here
#Execute Tkinter
root.mainloop()