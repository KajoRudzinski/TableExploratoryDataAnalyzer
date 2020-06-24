from tkinter import ttk
from tkinter import filedialog
from tkinter import *

csv_filetypes = ("csv files", "*.csv")
txt_filetypes = ("txt files", "*.txt")


def accepted_filetypes():
    return csv_filetypes, txt_filetypes


def browse_file():
    filepath = filedialog.askopenfilename(
        initialdir="/",
        title="Select file with your data",
        filetypes=accepted_filetypes())
    print(filepath)


def run_gui():
    root = Tk()
    button_read_file = ttk.Button(text="Read file", command=browse_file)
    button_read_file.grid(column=1, row=1)
    root.mainloop()
