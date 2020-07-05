from src import gui, msg, io

status = None
dataset = None
error = None


def get_accepted_filetypes():
    return io.FileReader().accepted_filetypes


def read_data_from_file(filepath: str):
    global dataset
    global status

    f = io.FileReader(filepath)
    f.read()
    dataset = f.data

    status.update_to_file_read_ok()


class Status:
    def __init__(self):
        self._prefix = "Status: "

        # available status
        self._initial_status = "Ready for work"
        self._file_read_ok = "File read correctly"

        self.current_status = self._format(self._initial_status)

    def _format(self, status: str):
        return f"{self._prefix}{status}"

    def update_to_file_read_ok(self):
        self.current_status = self._format(self._file_read_ok)


def get_current_status():
    global status
    return status.current_status


def run():
    print(msg.start_app_msg())

    global status
    status = Status()

    gui.run_gui()

    print(msg.close_app_msg())

