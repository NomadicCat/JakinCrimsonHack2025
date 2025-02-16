import threading
import time
import tkinter as tk
import hand_recon
#from tkinter import ttk
running = False
background_thread = None

def background_program():
    while running:


# Create the root window
root = tk.Tk()

# Set the window size and title
root.geometry("700x500")
root.title("Interface")

# Add a label with the text "no hands"
main_screen = tk.Label(root, text="no hands", font=("Helvetica", 80, "bold"))
main_screen.place(relx=.5, y=100, anchor=tk.CENTER)



# Define the function to be triggered by the button
def on_button_click():
    global running, background_thread
    # Check the current button text and toggle it
    if button.cget("text") == "enable":
        button.config(text="disable")  # Change text to "Disable"

        if not running:
            running = True
            background_thread = threading.Thread(target=background_program)
            background_thread.daemon = True
            background_thread.start()

    else:
        button.config(text="enable")  # Change text to "Enable"

        running = False
        if background_thread is not None:
            background_thread = None


# Add a button to the window
button = tk.Button(root, text="enable", font=("Helvetica", 40), command=on_button_click)
button.place(x=200, y=190, width=200, height=100)

settings_window = tk.Frame(root)

def open_settings():
    settingsButton.place_forget()
    settings_window.pack(fill="both", expand=True)
    main_screen.place_forget()
    returnButton.pack(side=tk.BOTTOM, pady=20)


def return_to_main():
    main_screen.place(relx=.5, y=100, anchor=tk.CENTER)
    settings_window.pack_forget()
    returnButton.pack_forget()
    settingsButton.place(x=400, y=190, height=100, width=100)


settingsButton=tk.Button(root, text="⚙", font=("Helvetica", 40), command=open_settings)
settingsButton.place(x=400, y=190, height=100, width=100)

returnButton = tk.Button(settings_window, text="return", font=("Helvetica", 20), command=return_to_main)

# Start the Tkinter event loop
root.mainloop()
