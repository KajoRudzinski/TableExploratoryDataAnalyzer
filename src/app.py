from src import msg_formats_graphics as mfg
from src import gui


def filepath_provided_by_the_user(filepath):
    print(type(filepath))


def run():
    print(mfg.start())
    gui.run_gui()
    print(mfg.end())
