from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from src import app

csv_files = ("csv files", "*.csv")
txt_files = ("txt files", "*.txt")


def pass_filepath_to_app(filepath):
    app.filepath_provided_by_the_user(filepath)


def accepted_fileTypes():
    return csv_files, txt_files


class GUI(Tk):
    def __init__(self):
        super(GUI, self).__init__()
        self.title("Table Exploratory Data Analyzer")
        self.minsize(640, 400)

        # self.wm_iconbitmap('icon.ico')
        self.labelFrame_SelectFile = None
        self.button_SelectFile = None

        self.setup_gui_style()
        self.create_labelFrame_SelectFile()
        self.create_button_SelectFile()

        self.selected_filePath = None

    @staticmethod
    def setup_gui_style():
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")

    def create_labelFrame_SelectFile(self):
        self.labelFrame_SelectFile = ttk.LabelFrame(self, text="Open File")
        self.labelFrame_SelectFile.grid(column=0, row=1, padx=20, pady=20)

    def create_button_SelectFile(self):
        self.button_SelectFile = ttk.Button(self.labelFrame_SelectFile, text="Browse A File", command=self.fileDialog)
        self.button_SelectFile.grid(column=1, row=1)

    def fileDialog(self):
        self.selected_filePath = filedialog.askopenfilename(
            initialdir="/",
            title="Select A File",
            filetype=accepted_fileTypes())


def run_gui():
    gui = GUI()
    gui.mainloop()
