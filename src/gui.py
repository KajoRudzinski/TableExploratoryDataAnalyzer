from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from src import app

csv_filetypes = ("csv files", "*.csv")
txt_filetypes = ("txt files", "*.txt")


def pass_filepath_to_app(filepath):
    app.filepath_provided_by_the_user(filepath)


def accepted_filetypes():
    return csv_filetypes, txt_filetypes


def browse_file():
    filepath = filedialog.askopenfilename(
        initialdir="/",
        title="Select file with your data",
        filetypes=accepted_filetypes())
    pass_filepath_to_app(filepath)


def run_gui():
    root = Tk()
    button_read_file = ttk.Button(text="Read file", command=browse_file)
    status_label = ttk.Label(textvariable="status")
    button_read_file.grid(column=1, row=1)
    status_label.grid(column=1, row=3)
    root.mainloop()
