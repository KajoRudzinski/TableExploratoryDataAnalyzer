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
        self.minsize(800, 600)
        # self.wm_iconbitmap('icon.ico')
        self.setup_guiStyle()

        # variables
        self.mainAppStatus = StringVar()

        # main frames
        self.upperFrame = None
        self.middleFrame = None
        self.lowerFrame = None

        self.load_upperFrame()
        self.load_middleFrame()
        self.load_lowerFrame()

        # upperFrame elements
        self.labelFrame_selectFile = None
        self.button_selectFile = None
        self.labelFrame_status = None

        self.create_labelFrame_selectFile()
        self.create_button_selectFile()
        self.create_label_status()

        self.selected_filePath = None

    @staticmethod
    def setup_guiStyle():
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")

    def load_upperFrame(self):
        self.upperFrame = Frame(self, bg="blue")
        self.upperFrame.place(
            relx=0.5, relwidth=1, relheight=0.1, anchor="n")

    def load_middleFrame(self):
        self.middleFrame = Frame(
            self, bg="green")
        self.middleFrame.place(
            relx=0.5, rely=0.5, relwidth=0.9, relheight=0.7, anchor="center")

    def load_lowerFrame(self):
        self.lowerFrame = Label(self, bg="blue", )
        self.lowerFrame.place(relx=0.5, rely=1, relwidth=1, relheight=0.1, anchor='s')

    def create_labelFrame_selectFile(self):
        self.labelFrame_selectFile = ttk.LabelFrame(self, text="Open File")
        self.labelFrame_selectFile.grid(column=0, row=1)

    def create_label_status(self):
        self.labelFrame_status = ttk.Label(self, text="welcome", relief="sunken")
        self.labelFrame_status.grid(column=2, row=1, padx=10)

    def create_button_selectFile(self):
        self.button_selectFile = ttk.Button(self.labelFrame_selectFile, text="Browse A File", command=self.fileDialog)
        self.button_selectFile.grid(column=1, row=1)

    def fileDialog(self):
        self.selected_filePath = filedialog.askopenfilename(
            initialdir="/",
            title="Select A File",
            filetype=accepted_fileTypes())


def run_gui():
    gui = GUI()
    gui.mainloop()

