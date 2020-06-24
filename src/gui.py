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
    return filepath


root = Tk()
root.filename = browse_file()
print(root.filename)
root.mainloop()
