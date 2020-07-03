from src import io

valid_paths = ["empty_file.txt", "valid.csv"]
invalid_paths = ["nope", 5, True]


def test_filereader_accepts_valid_path():
    for f in valid_paths:
        x = io.FileReader(f)
        assert x.path_is_accepted is True


def test_filereader_doesnt_accept_invalid_path():
    for f in invalid_paths:
        x = io.FileReader(f)
        assert x.path_is_accepted is False
