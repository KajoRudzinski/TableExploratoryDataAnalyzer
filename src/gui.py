from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from src import app

csv_files = ("csv files", "*.csv")
txt_files = ("txt files", "*.txt")


def pass_filepath_to_app(filepath):
    app.filepath_provided_by_the_user(filepath)


def accepted_filetypes():
    return csv_files, txt_files


class GUI(Tk):
    def __init__(self):
        super(GUI, self).__init__()
        self.title("Table Exploratory Data Analyzer")
        self.minsize(800, 600)
        # self.wm_iconbitmap('icon.ico')

        # variables
        self.font_default = ("Gotham", 9, "normal")
        self.app_status = StringVar()
        self.app_status.set("Status: Ready. Awaiting for a file to analyse.")

        # main frames
        self.fr_header = None
        self.fr_body = None
        self.fr_footer = None

        self.load_fr_header()
        self.load_fr_body()
        self.load_fr_footer()

        # upperFrame elements
        self.btt_select_file = None
        self.btt_save_to_file = None
        self.lfr_status = None
        self.lbl_status_text = None

        self.load_btt_select_file()
        self.load_btt_save_to_file()
        self.load_lfr_status()
        self.load_lbl_status_text()

        self.selected_file = None

        self.setup_gui_style()

    def setup_gui_style(self):
        ttk.Style().configure("TButton", relief="flat", font=self.font_default)

    # header
    def load_fr_header(self):
        self.fr_header = Frame(self, bg="#0c0e1a")
        self.fr_header.place(
            relx=0.5, relwidth=1, height=50, anchor="n")

    # header elements

    def load_btt_select_file(self):
        self.btt_select_file = ttk.Button(self.fr_header, text="Open File", command=self.select_file)
        self.btt_select_file.pack(side=LEFT, anchor=CENTER, padx=10)

    def load_btt_save_to_file(self):
        # TODO Now only opening file dialog, saving file not yet implemented
        self.btt_save_to_file = ttk.Button(self.fr_header, text="Save Analysis", command=self.select_file)
        self.btt_save_to_file.pack(side=LEFT, anchor=CENTER, padx=10)

    def load_lfr_status(self):
        self.lfr_status = Label(self.fr_header)
        self.lfr_status.pack(side=LEFT, anchor=W, ipadx=10, padx=10, pady=5)

    def load_lbl_status_text(self):
        self.lbl_status_text = Label(self.lfr_status, textvariable=self.app_status, font=self.font_default)
        self.lbl_status_text.pack(side=RIGHT, fill=BOTH, expand=1, anchor=CENTER)

    # button functions
    def select_file(self):
        self.selected_file = filedialog.askopenfilename(
            initialdir="/",
            title="Select A File",
            filetype=accepted_filetypes())

    # body
    def load_fr_body(self):
        self.fr_body = Frame(
            self, bg="#0c0e1a")
        self.fr_body.place(
            relx=0.5, rely=0.5, relwidth=0.9, relheight=0.7, anchor="center")

    # footer
    def load_fr_footer(self):
        self.fr_footer = Label(self, bg="#0c0e1a", )
        self.fr_footer.place(relx=0.5, rely=1, relwidth=1, height=50, anchor='s')


def run_gui():
    gui = GUI()
    gui.mainloop()

