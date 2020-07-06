import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
from src import app
gui = None


def run_gui():
    global gui
    gui = GUI()
    gui.mainloop()


def choose_file_to_analyse():
    filepath = get_filepath_from_filedialog()
    if filepath != "":
        app.read_data_from_file(filepath)
    update_status()
    update_response()


def get_filepath_from_filedialog():
    filepath = filedialog.askopenfilename(
        initialdir="/",
        title="Select A File",
        filetype=get_accepted_filetypes_tuple())
    return filepath


def save_analysis_to_file():
    pass


def get_accepted_filetypes_tuple():
    accepted_filetypes_list = []
    for x in app.get_accepted_filetypes():
        y = "{} files".format(x), "*.{}".format(x)
        accepted_filetypes_list.append(y)
    return tuple(accepted_filetypes_list)


def update_status():
    global gui
    gui.header.current_app_status.set(app.get_current_status())


def update_response():
    delete_currently_displayed_response()
    load_response_from_app()


def delete_currently_displayed_response():
    global gui
    gui.body.response_text.delete('1.0', tk.END)


def load_response_from_app():
    global gui
    gui.body.response_text.insert(tk.INSERT, app.response_text)


def get_main_color():
    return "#0c0e1a"


def get_main_font():
    return "Gotham", 9, "normal"


class GUI(tk.Tk):
    """ Graphic User Interface constructed out of Header, Body and Footer"""
    def __init__(self):
        super(GUI, self).__init__()
        self.title(app.app_name)
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
        self.header.place(relx=0.5, relwidth=1, height=50, anchor=tk.N)

    def load_body(self):
        self.body.place(
            relx=0.5, rely=0.5, relwidth=0.9, relheight=0.7, anchor=tk.CENTER)

    def load_footer(self):
        self.footer.place(relx=0.5, rely=1, relwidth=1, height=50, anchor=tk.S)

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
            window_width, window_height,
            self.center_width(window_width),
            self.center_height(window_height)))

    def center_height(self, height):
        return (self.winfo_screenheight() // 2) - (height // 2)

    def center_width(self, width):
        return (self.winfo_screenwidth() // 2) - (width // 2)


class Header(tk.Frame):
    """ Upper side of GUI. Contains buttons to open file, save analysis
    and a status information"""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=get_main_color())
        self.parent = parent

        # buttons open & save
        self.button_open_file = ttk.Button(
            self, text="Open File", command=choose_file_to_analyse)

        self.button_save_to_file = ttk.Button(
            self, text="Save Analysis", command=save_analysis_to_file)

        # status label
        self.current_app_status = tk.StringVar()
        self.current_app_status.set(app.get_current_status())

        self.status_container = tk.Label(self)
        self.status = tk.Label(
            self.status_container,
            textvariable=self.current_app_status,
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
    """Central part of GUI. Contains space for analysis result
    (currently text only)"""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=get_main_color())
        self.parent = parent

        self.fr_response = tk.Frame(self)

        self.response_text = tk.scrolledtext.ScrolledText(
            self.fr_response, wrap=tk.WORD, width=20, height=10,
            font=get_main_font())

        self.load_body_widgets()

    def load_body_widgets(self):
        self.load_fr_response()
        self.load_response_text()

    def load_fr_response(self):
        self.fr_response.place(
            relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor=tk.CENTER)

    def load_response_text(self):
        self.response_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.load_initial_response()

    def load_initial_response(self):
        self.response_text.insert(tk.INSERT, app.response_text)


class Footer(tk.Frame):
    """Goes on the bottom of the GUI. Space for authorship information,
    release date, etc."""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=get_main_color())
        self.parent = parent
