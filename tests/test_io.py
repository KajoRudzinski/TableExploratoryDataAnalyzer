from src import io
import os

data = "C1, C2\n1, 2"
empty_file = "empty.txt"
valid_csv = "valid.csv"

valid_paths = [empty_file, valid_csv]
invalid_paths = ["nope", 5, True]


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


def test_filereader_accepts_valid_path():
    create_2_main_test_files()
    for f in valid_paths:
        assert io.FileReader(f).path_is_accepted is True
    remove_test_files()


def test_filereader_doesnt_accept_invalid_path():
    for f in invalid_paths:
        assert io.FileReader(f).path_is_accepted is False


def test_filereader_retreives_filename_from_path():
    assert io.FileReader("E:/x.csv").file_name == "x.csv"
    assert io.FileReader("E:/data/x.csv").file_name == "x.csv"


def test_filereader_starts_without_data_or_error():
    for f in invalid_paths+invalid_paths:
        assert io.FileReader(f).data is None
        assert io.FileReader(f).error is None
        assert io.FileReader(f).error_msg is None


def test_filereader_returns_error_if_filepath_not_accepted():
    for f in invalid_paths:
        fr = io.FileReader(f)
        assert fr.path_is_accepted is False


def test_filereader_empty_file_gives_error():
    create_test_file(empty_file)
    f = io.FileReader(empty_file)
    f.read()
    assert f.error is not None
    remove_test_files()


def test_filereader_valid_file_returns_data():
    create_test_file(valid_csv, filedata=data)
    f = io.FileReader(valid_csv)
    f.read()
    assert f.data is not None
    remove_test_files()
