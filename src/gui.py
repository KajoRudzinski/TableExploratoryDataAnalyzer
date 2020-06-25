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

        self.app_status = StringVar()

        # self.wm_iconbitmap('icon.ico')
        self.labelFrame_SelectFile = None
        self.labelFrame_Status = None
        self.button_SelectFile = None
        
        # To be changed to set appropriate column and row weight and padding
        # self.columnconfigure(1, weight=1)
        # self.columnconfigure(3, pad=7)
        # self.rowconfigure(3, weight=1)
        # self.rowconfigure(5, pad=7)

        self.setup_gui_style()
        self.create_labelFrame_selectFile()
        self.create_label_status()
        self.create_button_selectFile()

        self.selected_filePath = None

    @staticmethod
    def setup_gui_style():
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")

    def create_labelFrame_selectFile(self):
        self.labelFrame_SelectFile = ttk.LabelFrame(self, text="Open File")
        self.labelFrame_SelectFile.grid(column=0, row=1)

    def create_label_status(self):
        self.labelFrame_Status = ttk.Label(self, text="welcome", relief="sunken")
        self.labelFrame_Status.grid(column=2, row=1, padx=10)

    def create_button_selectFile(self):
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

