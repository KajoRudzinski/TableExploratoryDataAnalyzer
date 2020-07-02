import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from src import app
from src import msg


def run_gui():
    gui = GUI()
    gui.mainloop()


def open_file():
    selected_file = filedialog.askopenfilename(
        initialdir="/",
        title="Select A File",
        filetype=app.accepted_filetypes())
    app.filepath_provided_by_the_user(selected_file)


def save_file():
    pass


def get_main_color():
    return "#0c0e1a"


def get_main_font():
    return "Gotham", 9, "normal"


class GUI(tk.Tk):
    def __init__(self):
        super(GUI, self).__init__()
        self.title(msg.get_app_name())
        self.width = 800
        self.height = 600
        self.set_size()
        self.center_window(self.width, self.height)

        self.font_default = get_main_font()
        self.setup_gui_style()

        self.header = Header(self)
        self.body = Body(self)
        self.footer = Footer(self)
        self.load_gui_widgets()

    def load_gui_widgets(self):
        self.load_header()
        self.load_body()
        self.load_footer()

    def load_header(self):
        self.header.place(
            relx=0.5,
            relwidth=1,
            height=50,
            anchor=tk.N)

    def load_body(self):
        self.body.place(
            relx=0.5,
            rely=0.5,
            relwidth=0.9,
            relheight=0.7,
            anchor=tk.CENTER)

    def load_footer(self):
        self.footer.place(
            relx=0.5,
            rely=1,
            relwidth=1,
            height=50,
            anchor=tk.S)

    def setup_gui_style(self):
        ttk.Style().configure(
            "TButton", relief="flat", font=self.font_default)

    def set_size(self):
        self.minsize(self.width, self.height)

    def center_window(self, width: int, height: int, toplevel=None):
        self.update_idletasks()
        if toplevel is None:
            self.center_main_window(height, width)
        else:
            self.center_selected_window(toplevel, height, width)

    def center_main_window(self, height, width):
        self.center_selected_window(self, height, width)

    def center_selected_window(self, window, window_height, window_width):
        window.geometry('{}x{}+{}+{}'.format(
            window_width,
            window_height,
            self.center_width(window_width),
            self.center_height(window_height)))

    def center_height(self, height):
        return (self.winfo_screenheight() // 2) - (height // 2)

    def center_width(self, width):
        return (self.winfo_screenwidth() // 2) - (width // 2)


class Header(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=get_main_color())
        self.parent = parent

        # buttons open & save
        self.button_open_file = ttk.Button(
            self, text="Open File", command=open_file)

        self.button_save_to_file = ttk.Button(
            self, text="Save Analysis", command=save_file)

        # status label
        self.app_status = tk.StringVar()
        self.app_status.set(msg.get_initial_status())

        self.status_container = tk.Label(self)
        self.status = tk.Label(
            self.status_container,
            textvariable=self.app_status,
            font=get_main_font())

        self.load_header_widgets()

    def load_header_widgets(self):
        self.load_button_open_file()
        self.load_button_save_to_file()
        self.load_status_container()
        self.load_status()

    def load_button_open_file(self):
        self.button_open_file.pack(
            side=tk.LEFT, anchor=tk.CENTER, padx=10)

    def load_button_save_to_file(self):
        self.button_save_to_file.pack(
            side=tk.LEFT, anchor=tk.CENTER, padx=10)

    def load_status_container(self):
        self.status_container.pack(
            side=tk.LEFT, anchor=tk.W, ipadx=10, padx=10, pady=5)

    def load_status(self):
        self.status.pack(
            side=tk.RIGHT, fill=tk.BOTH, expand=1, anchor=tk.CENTER)


class Body(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=get_main_color())
        self.parent = parent

        self.app_response = tk.StringVar()
        self.app_response.set(msg.get_initial_text_response())

        self.fr_response = tk.Frame(self)
        self.fr_for_scrollable_canvas = tk.Frame(self.fr_response)
        self.scrollable_canvas = tk.Canvas(self.fr_for_scrollable_canvas)

        self.scrollbar = ttk.Scrollbar(
            self.fr_for_scrollable_canvas,
            orient=tk.VERTICAL,
            command=self.scrollable_canvas.yview)

        self.scrollable_frame = ttk.Frame(self.scrollable_canvas)

        self.load_body_widgets()

        self.bind_scrollable_canvas_to_scrolling_action()

        self.response_txt = ttk.Label(
            self.scrollable_frame,
            textvariable=self.app_response,
            font=get_main_font())

        # response text has to loaded after
        # the setup of the scrollable canvas and configuring scrolling action
        self.load_response_text()

    def load_body_widgets(self):
        self.load_fr_response()
        self.load_fr_for_scrollable_canvas()
        self.load_scrollable_canvas()
        self.load_scrollbar()

    def load_fr_response(self):
        self.fr_response.place(
            relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor=tk.CENTER)

    def load_fr_for_scrollable_canvas(self):
        self.fr_for_scrollable_canvas.pack(
            side=tk.LEFT, fill=tk.BOTH, expand=1, anchor=tk.CENTER)

    def load_scrollable_canvas(self):
        self.scrollable_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def load_scrollbar(self):
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def configure_scrollable_canvas(self):
        self.scrollable_canvas.configure(
            scrollregion=self.scrollable_canvas.bbox("all"))

    def bind_scrollable_canvas_to_scrolling_action(self):
        self.scrollable_frame.bind("<Configure>", self.configure_scrollable_canvas())
        self.scrollable_canvas.create_window((0, 0), window=self.scrollable_frame, anchor=tk.NW)
        self.scrollable_canvas.configure(yscrollcommand=self.scrollbar.set)

    def load_response_text(self):
        self.response_txt.pack()


class Footer(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=get_main_color())
        self.parent = parent
