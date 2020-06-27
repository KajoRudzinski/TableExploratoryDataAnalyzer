from src import msg
from src import gui


def filepath_provided_by_the_user(filepath: str) -> str:
    """
    Returns path to a file of accepted file type.
    Accepted file type is enforced by GUI.
    """
    print(filepath)
    return filepath


def accepted_filetypes() -> tuple:
    """
    Returns file types that can be analysed by the application.
    Used by GUI.
    """
    return ("csv files", "*.csv"),  ("txt files", "*.txt")


def run():
    print(msg.start_app_msg())
    gui.run_gui()
    print(msg.close_app_msg())

