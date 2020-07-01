from src import msg
from src import gui


def filepath_provided_by_the_user(filepath: str) -> str:
    print(filepath)
    return filepath


def accepted_filetypes() -> tuple:
    return ("csv files", "*.csv"),  ("txt files", "*.txt")


def run():
    print(msg.start_app_msg())
    gui.run_gui()
    print(msg.close_app_msg())

