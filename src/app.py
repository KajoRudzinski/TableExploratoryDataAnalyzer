from src import gui, msg, io

status = None
dataset = None
error = None
response_text = msg.get_initial_text_response()
app_name = msg.get_app_name()


def get_accepted_filetypes():
    return io.FileReader().accepted_filetypes


def read_data_from_file(filepath: str):
    global dataset
    global status
    global response_text

    f = io.FileReader(filepath)
    f.read()

    if f.data is not None:
        status.update_to_file_read_ok()
        dataset = f.data
        response_text = dataset.to_string()

    if f.error is not None:
        status.update_to_error(f.error_msg)


class Status:
    def __init__(self):
        self._prefix = "Status: "

        # available status
        self._initial_status = "Ready for work"
        self._file_read_ok = "File read correctly"
        self._error = "Error. "
        self.current_status = self._format(self._initial_status)

    def _format(self, status: str):
        return f"{self._prefix}{status}"

    def update_to_file_read_ok(self):
        self.current_status = self._format(self._file_read_ok)

    def update_to_error(self, error_msg: str):
        full_error = "{}{}".format(self._error, error_msg)
        self.current_status = self._format(full_error)

def get_current_status():
    global status
    return status.current_status


def run():
    print(msg.start_app_msg())

    global status
    status = Status()

    gui.run_gui()

    print(msg.close_app_msg())

