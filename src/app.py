from src import gui, msg, io


def get_accepted_filetypes():
    return io.FileReader().accepted_filetypes


def filepath_provided_by_the_user(filepath: str):
    f = io.FileReader(filepath)
    f.read()
    print(f.data)




def run():
    print(msg.start_app_msg())
    gui.run_gui()
    print(msg.close_app_msg())

