import pandas as pd
from pandas import errors as epd


class Importer:

    def __init__(self):
        self.file_path = None
        self.file_delimiter = None
        self.dataset = None
        self.error = None

    empty_file_error = "The file is empty"
    no_file_error = "The file doesn't exist"

    def set_file_path(self, file_path: str):
        self.file_path = file_path

    def set_delimiter(self, delimiter):
        self.file_delimiter = delimiter

    def read_csv_file(self):
        try:
            self.dataset = pd.read_csv(
                self.file_path, sep=self.file_delimiter)
        except epd.EmptyDataError:
            self.error = self.empty_file_error
        except FileNotFoundError:
            self.error = self.no_file_error
