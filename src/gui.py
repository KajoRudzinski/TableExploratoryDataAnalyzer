from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from src import app
from src import msg


class GUI(Tk):
    def __init__(self):
        super(GUI, self).__init__()
        self.title(msg.app_title)
        self.min_main_window_width = 800
        self.min_main_window_height = 600
        self.minsize(self.min_main_window_width, self.min_main_window_height)
        self.center_window(self.min_main_window_width, self.min_main_window_height)



        # self.wm_iconbitmap('icon.ico')

        # variables #
        self.font_default = ("Gotham", 9, "normal")

        self.app_status = StringVar()
        self.app_status.set(msg.initial_status)

        self.app_response = StringVar()
        self.app_response.set(msg.initial_text_response)

        self.question = None

        # gui elements #

        # header
        self.header = self.get_main_frame(self)
        self.header.place(
            relx=0.5,
            relwidth=1,
            height=50,
            anchor="n")

        # header # open file button
        self.button_open_file = ttk.Button(
            self.header,
            text="Open File",
            command=self.select_file)

        self.button_open_file.pack(
            side=LEFT,
            anchor=CENTER,
            padx=10)

        # header # save file button
        self.button_save_to_file = ttk.Button(
            self.header,
            text="Save Analysis",
            command=self.select_file)

        self.button_save_to_file.pack(
            side=LEFT,
            anchor=CENTER,
            padx=10)

        # header # frame for status
        self.frame_for_status = Label(self.header)
        self.frame_for_status.pack(
            side=LEFT,
            anchor=W,
            ipadx=10,
            padx=10,
            pady=5)

        # header # frame for status # status
        self.status = Label(
            self.frame_for_status,
            textvariable=self.app_status,
            font=self.font_default)

        self.status.pack(
            side=RIGHT,
            fill=BOTH,
            expand=1,
            anchor=CENTER)

        # body
        self.body = self.get_main_frame(self)
        self.body.place(
            relx=0.5,
            rely=0.5,
            relwidth=0.9,
            relheight=0.7,
            anchor=CENTER)

        # body # response frame
        self.fr_response = self.get_main_frame(self.body)
        self.fr_response.place(
            relx=0.5,
            rely=0.5,
            relwidth=0.9,
            relheight=0.9,
            anchor=CENTER)

        # body # response frame # frame for scrollable canvas
        self.fr_for_scrollable_canvas = ttk.Frame(self.fr_response)
        self.fr_for_scrollable_canvas.pack(
            side=LEFT,
            fill=BOTH,
            expand=1,
            anchor=CENTER)

        # body # response frame # frame for scrollable canvas
        # scrollable canvas
        self.scrollable_canvas = Canvas(self.fr_for_scrollable_canvas)
        self.scrollable_canvas.pack(
            side="left",
            fill="both",
            expand=True)

        # body # response frame # frame for scrollable canvas
        # scrollable canvas # scrollbar
        self.scrollbar = ttk.Scrollbar(
            self.fr_for_scrollable_canvas,
            orient="vertical",
            command=self.scrollable_canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # body # response frame # frame for scrollable canvas
        # scrollable canvas # scrollable frame
        self.scrollable_frame = ttk.Frame(self.scrollable_canvas)
        self.scrollable_frame.bind(
            "<Configure>", lambda e: self.scrollable_canvas.configure(
                scrollregion=self.scrollable_canvas.bbox("all")))

        # body # response frame # frame for scrollable canvas
        # scrollable canvas configuration
        self.scrollable_canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw")

        self.scrollable_canvas.configure(
            yscrollcommand=self.scrollbar.set)

        # body # response frame # frame for scrollable canvas
        # scrollable canvas # scrollable frame # response txt
        self.response_txt = ttk.Label(
            self.scrollable_frame,
            textvariable=self.app_response, font=self.font_default).pack()

        # footer
        self.footer = self.get_main_frame(self)
        self.footer.place(
            relx=0.5,
            rely=1,
            relwidth=1,
            height=50,
            anchor='s')

        self.setup_gui_style()

    def setup_gui_style(self):
        ttk.Style().configure(
            "TButton", relief="flat", font=self.font_default)

    def center_window(self, window_width: int, window_height: int, window=None):
        self.update_idletasks()
        if window is None:
            self.center_main_window(window_height, window_width)
        else:
            self.center_selected_window(window, window_height, window_width)

    def center_selected_window(self, window, window_height, window_width):
        window.geometry('{}x{}+{}+{}'.format(
            window_width,
            window_height,
            self.center_width(window_width),
            self.center_height(window_height)))

    def center_main_window(self, window_height, window_width):
        self.center_selected_window(self, window_height, window_width)

    def center_height(self, window_height):
        return (self.winfo_screenheight() // 2) - (window_height // 2)

    def center_width(self, window_width):
        return (self.winfo_screenwidth() // 2) - (window_width // 2)

    @staticmethod
    def get_main_frame(parent):
        return Frame(parent, bg="#0c0e1a")

    def select_file(self):

        while self.question is None:

            selected_file = filedialog.askopenfilename(
                initialdir="/",
                title="Select A File",
                filetype=app.accepted_filetypes())
            app.filepath_provided_by_the_user(selected_file)

            self.question = Toplevel()
            w = 600
            h = 300
            self.question.minsize(w, h)
            self.question.focus_force()
            self.question.lift(aboveThis=self)
            self.center_window(w, h, self.question)

            delimiter_label = Label(
                self.question,
                text="\tColumn delimiter (usually , or ;): ",
                height=4)
            delimiter_label.pack(side=LEFT)

            delimiter_entry=Entry(self.question, text="", width=50)
            delimiter_entry.pack(side=LEFT)




def run_gui():
    gui = GUI()
    gui.mainloop()

