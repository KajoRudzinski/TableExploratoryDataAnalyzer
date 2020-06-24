from src import msg, gui


def run():
    print(msg.start())
    gui.run_gui()
    print(msg.end())
