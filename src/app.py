from src import gui, msg, io

app_name = msg.get_app_name()
status = msg.format_status("Ready to work")
response_text = msg.get_response_text_initial()
dataset = None


def update_status(s: str):
    global status
    status = s


def update_dataset(d):
    global dataset
    dataset = d


def update_response_text(r: str):
    global response_text
    response_text = r


def get_accepted_filetypes():
    return io.FileReader().accepted_filetypes


def read_data_from_file(filepath: str):
    f = io.FileReader(filepath)
    f.read()

    if f.data is not None:
        update_dataset(f.data)
        update_status(msg.format_status("File read correctly"))
        update_response_text(msg.get_response_text_file_read_ok(f.file_name))

    if f.error is not None:
        update_status(msg.format_status(f.error_msg, error=True))
        update_response_text(msg.get_response_text_error())


def run():
    print(msg.start_app_msg())
    gui.run_gui()
    print(msg.close_app_msg())

