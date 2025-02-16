import tkinter as tk
from tkinter import ttk

# Create the root window
root = tk.Tk()

# Set the window size and title
root.geometry("700x500")
root.title("Interface")

# Add a label with the text "no hands"
label = tk.Label(root, text="no hands", font=("Helvetica_bold", 70))
label.pack(padx=20, pady=20)

# Define the function to be triggered by the button
def on_button_click():
    # Check the current button text and toggle it
    if button.cget("text") == "enable":
        button.config(text="disable")  # Change text to "Disable"
    else:
        button.config(text="enable")  # Change text to "Enable"


# Add a button to the window
button = tk.Button(root, text="enable", font=("Helvetica", 40), command=on_button_click)
button.pack(pady=20)
button.place(x=250, y=190, width=200, height=100)

# Start the Tkinter event loop
root.mainloop()
