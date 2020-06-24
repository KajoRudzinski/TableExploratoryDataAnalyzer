from src import msg, gui

def filepath_provided_by_the_user(filepath):
    print(type(filepath))

def run():
    print(msg.start())
    gui.run_gui()
    print(msg.end())
