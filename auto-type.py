import time
import random
import importlib
import subprocess

# Check if pyautogui is installed, and install it if it is not
try:
    importlib.import_module('pyautogui')
except ImportError:
    subprocess.check_call(['pip', 'install', 'pyautogui'])
    importlib.import_module('pyautogui')

# Check if tkinter is installed, and install it if it is not
try:
    importlib.import_module('tkinter')
except ImportError:
    subprocess.check_call(['pip', 'install', 'tkinter'])
    importlib.import_module('tkinter')

from tkinter import Tk, simpledialog, Label, Button
import pyautogui

# Define the list of messages to randomly select from
message_list = ["hi", "yo", "lol", "lmao", "OMG", "lets go", "nice", "wow", "thats cool", "Yeah", "Ayo", "LAMO", "sound great", "DAMN", "Cool"]

# Create a dialog box to prompt the user for the interval time (in minutes)
root = Tk()
root.withdraw()
interval_dialog = simpledialog.askinteger(title="Auto Typer", prompt="Enter the interval time in minutes:")
root.deiconify()
root.lift()

# Convert the interval time from minutes to seconds
interval = interval_dialog * 60

# Define a function to stop the auto typer
def stop_autotyper():
    root.destroy()

# Create a label to display the time until the next auto type
time_label = Label(root, text="")
time_label.pack()

# Create an "End" button to stop the auto typer
stop_button = Button(root, text="End", command=stop_autotyper)
stop_button.pack()

# Loop indefinitely
while True:
    # Select a random message from the list
    message = random.choice(message_list)

    # Type the message
    pyautogui.typewrite(message)

    # Press enter
    pyautogui.press("enter")

    # Calculate the time until the next auto type
    remaining_time = interval
    while remaining_time > 0:
        time_label.config(text="Next auto type in {} seconds".format(remaining_time))
        root.update()
        time.sleep(1)
        remaining_time -= 1

    # Update the time label to show that the next auto type is happening
    time_label.config(text="Auto typing...")

    # Wait for a short time before selecting the next message
    time.sleep(2)

    # Check if the "End" button has been pressed
    root.update()
    if root.winfo_exists() == False:
        break
