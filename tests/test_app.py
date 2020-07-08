from src import app


def test_update_status():
    t = "x"
    app.update_status(t)
    assert app.status == t


def test_update_dataset():
    t = "x"
    app.update_dataset(t)
    assert app.dataset == t


def test_update_response_text():
    t = "x"
    app.update_response_text(t)
    assert app.response_text == t


def test_get_accepted_filetypes():
    assert app.get_accepted_filetypes() == app.io.FileReader().accepted_filetypes
