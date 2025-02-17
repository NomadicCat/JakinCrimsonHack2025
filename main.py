import threading
import time
import tkinter as tk
import sys
import cv2
import shared
from subprocess import call
#from tkinter import ttk
running = False
background_thread = None

sensitivity = 2.5



def update_sensitivity(value):
    shared.set_sensitivity(float(value))

def background_program():
    global running
    while running:

        call(["python", "handRecon.py"])
        time.sleep(0.1)

def start_background_program():
    global running, background_thread
    if not running:
        running = True
        background_thread = threading.Thread(target=background_program)
        background_thread.daemon = True  # Ensure thread exits with the main program
        background_thread.start()



def stop_background_program():
    global running
    if running:
        running = False
        # Wait for the thread to finish
        if background_thread is not None:
            background_thread.join()


if __name__ == "__main__":
    import threading

if threading.current_thread().name == "MainThread":
# Create the root window
    root = tk.Tk()

# Set the window size and title
    root.geometry("700x400")
    #root.resizable(False, False)
    root.title("Interface")

    # Add a label with the text "no hands"
    main_screen = tk.Label(root, text="blue hands", font=("Helvetica", 80, "bold"), fg="blue")
    main_screen.place(relx=.5, y=100, anchor=tk.CENTER)
    subtext = tk.Label(root, text="developed by Team Jakin", font=("Helvetica", 20, "bold"))
    subtext.place(relx=.5, y=165, anchor=tk.CENTER)
    subtext2 = tk.Label(root, text="for Crimson Code 2025", font=("Helvetica", 15))
    subtext2.place(relx=.5, y=195, anchor=tk.CENTER)



    # Define the function to be triggered by the button
    def on_button_click():
        global running, background_thread
        # Check the current button text and toggle itblue
        if button.cget("text") == "enable":
            button.config(text="Q to exit",
            font=("Helvetica", 35))# Change text to "Q to exit"

            if not running:
                running = True
                background_thread = threading.Thread(target=background_program)
                background_thread.daemon = True
                background_thread.start()

        else:
            button.config(text="enable")  # Change text to "Enable"

            running = False
            if background_thread is not None:
                background_thread = False
                running = False
                sys.exit()



    # Add a button to the window
    button = tk.Button(root, text="enable", font=("Helvetica", 40), command=on_button_click)
    button.place(x=200, y=215, width=200, height=100)

    settings_window = tk.Frame(root)
    settings_window.pack_propagate(False)

    def open_settings():
        settingsButton.place_forget()
        settings_window.pack(fill="both", expand=True)
        trackbar.pack(pady=100, anchor="center")
        main_screen.place_forget()
        returnButton.pack(side=tk.BOTTOM, pady=20)



    def return_to_main():
        main_screen.place(relx=.5, y=100, anchor=tk.CENTER)
        settings_window.pack_forget()
        returnButton.pack_forget()
        settingsButton.place(x=400, y=215, height=100, width=100)


    trackbar = tk.Scale(settings_window, from_=0.5, to=5, orient=tk.HORIZONTAL,label="                                         adjust your sensitivity, bud", resolution=0.1, command=update_sensitivity, length=400)
    trackbar.set(sensitivity)  # Set default value


    settingsButton=tk.Button(root, text="⚙", font=("Helvetica", 40), command=open_settings)
    settingsButton.place(x=400, y=215, height=100, width=100)

    returnButton = tk.Button(settings_window, text="return", font=("Helvetica", 20), command=return_to_main)

    # Start the Tkinter event loop
    root.mainloop()
