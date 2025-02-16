import tkinter as tk
from tkinter import ttk

# Create the root window
root = tk.Tk()

# Set the window size and title
root.geometry("700x500")
root.title("Interface")

# Add a label with the text "no hands"
main_screen = tk.Label(root, text="no hands", font=("Helvetica_bold", 70))
main_screen.place(x=200, y=150)

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
button.place(x=200, y=190, width=200, height=100)

settings_window = tk.Frame(root)

def open_settings():
    settings_window.pack(fill="both", expand=True)
    settingsButton.pack_forget()
    main_screen.pack_forget()


def return_to_main():
    main_screen.place(x=200, y=150)
    settings_window.pack_forget()
    returnButton.pack_forget()
    settingsButton.place(x=400, y=190, height=100, width=100)

settingsButton=tk.Button(root, text="⚙", font=("Helvetica", 40), command=open_settings)
settingsButton.place(x=400, y=190, height=100, width=100)

returnButton = tk.Button(settings_window, text="return", font=("Helvetica", 25), command=return_to_main)
returnButton.pack(pady=20)
# Start the Tkinter event loop
root.mainloop()
