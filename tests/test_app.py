from src import app
import os

data = "C1, C2\n1, 2"
empty_file = "empty.txt"
valid_csv = "valid.csv"
valid_paths = [empty_file, valid_csv]


def create_test_file(filepath, filedata=""):
    f = open(filepath, "w")
    f.write(filedata)
    f.close()


def create_2_main_test_files():
    create_test_file(empty_file)
    create_test_file(valid_csv, filedata=data)


def remove_test_files():
    for f in valid_paths:
        try:
            os.remove(f)
        except FileNotFoundError:
            pass


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


def test_read_data_from_valid_file():
    create_test_file(valid_csv, filedata=data)
    app.read_data_from_file(valid_csv)
    assert app.dataset is not None
    assert valid_csv in app.response_text
    remove_test_files()


def test_read_data_from_empty_file():
    create_test_file(empty_file)
    app.read_data_from_file(empty_file)
    assert app.dataset is None
    assert "ERROR" in app.status
    remove_test_files()


def test_read_data_from_invalid_file():
    app.read_data_from_file("doesnt_exist")
    assert app.dataset is None
    assert "ERROR" in app.status


