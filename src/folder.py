import tkinter as tk
from ctypes import windll
from tkinter import filedialog


def open_folder() -> str:
    windll.shcore.SetProcessDpiAwareness(1)  # fixes the blurry file dialog

    root = tk.Tk()
    root.withdraw()
    root.attributes(
        "-topmost", True
    )  # Opened window will be above all other windows even if clicked off

    path_input = filedialog.askdirectory()

    # if you do not select a folder the first time, then select one, theres some error so just exit
    if len(path_input) < 1:
        print("Invalid Folder\n")
        exit()

    return path_input
