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

        # variables #
        self.font_default = ("Gotham", 9, "normal")

        self.app_status = StringVar()
        self.app_status.set("Status: Ready. Awaiting for a file to analyse.")

        self.app_response = StringVar()
        self.app_response.set("test \n"*30)

        self.selected_file = None

        # gui elements #

        # header
        self.fr_header = Frame(self, bg="#0c0e1a")
        self.fr_header.place(relx=0.5, relwidth=1, height=50, anchor="n")

        self.btt_select_file = ttk.Button(
            self.fr_header, text="Open File", command=self.select_file)
        self.btt_select_file.pack(side=LEFT, anchor=CENTER, padx=10)

        self.btt_save_to_file = ttk.Button(
            self.fr_header, text="Save Analysis", command=self.select_file)
        self.btt_save_to_file.pack(side=LEFT, anchor=CENTER, padx=10)

        self.lfr_status = Label(self.fr_header)
        self.lfr_status.pack(side=LEFT, anchor=W, ipadx=10, padx=10, pady=5)

        self.lbl_status_text = Label(
            self.lfr_status, textvariable=self.app_status, font=self.font_default)
        self.lbl_status_text.pack(side=RIGHT, fill=BOTH, expand=1, anchor=CENTER)

        # body
        self.fr_body = Frame(self, bg="#0c0e1a")
        self.fr_body.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.7, anchor="center")

        self.fr_response = Frame(self.fr_body, bg="green")
        self.fr_response.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor="center")

        self.fr_for_scrollable_canvas = ttk.Frame(self.fr_response)
        self.fr_for_scrollable_canvas.pack(side=LEFT, fill=BOTH, expand=1, anchor=CENTER)

        self.scrollable_canvas = Canvas(self.fr_for_scrollable_canvas)


        self.scrollbar = ttk.Scrollbar(self.fr_for_scrollable_canvas, orient="vertical", command=self.scrollable_canvas.yview)
        self.scrollable_frame = ttk.Frame(self.scrollable_canvas)

        self.scrollable_frame.bind(
            "<Configure>", lambda e: self.scrollable_canvas.configure(
                scrollregion=self.scrollable_canvas.bbox("all")))

        self.scrollable_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_canvas.configure(yscrollcommand=self.scrollbar.set)

        for i in range(50):
            ttk.Label(self.scrollable_frame, text="Sample scrolling label").pack()

        self.scrollable_canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.fr_footer = Label(self, bg="#0c0e1a", )
        self.fr_footer.place(relx=0.5, rely=1, relwidth=1, height=50, anchor='s')

        self.setup_gui_style()

    def setup_gui_style(self):
        ttk.Style().configure("TButton", relief="flat", font=self.font_default)

    def select_file(self):
        self.selected_file = filedialog.askopenfilename(
            initialdir="/",
            title="Select A File",
            filetype=accepted_filetypes())

def run_gui():
    gui = GUI()
    gui.mainloop()

