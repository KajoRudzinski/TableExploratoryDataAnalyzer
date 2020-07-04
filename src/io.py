from pandas import read_csv
from pandas.errors import EmptyDataError
import os


class FileReader:
    def __init__(self, path=None):
        self.path = str(path)
        self.accepted_filetypes = "csv", "txt"
        self.path_is_accepted = self.is_path_ok()
        self.data = None
        self.error = None
        self.error_msg = None

    def read(self):
        if self.path_is_accepted:
            self._get_data()
        else:
            self.error = True
            self.error_msg = "File path not accepted. File was not read"

    def _get_data(self):
        try:
            self.data = read_csv(self.path)
        except EmptyDataError:
            self.error = True
            self.error_msg = "The file is empty"
        except:
            self.error = True
            self.error_msg = "Unknown error while reading the file"

    def is_file_ok(self):
        if os.path.isfile(self.path):
            return True
        else:
            return False

    def is_filetype_ok(self):
        try:
            if self.path[-3:] in self.accepted_filetypes:
                return True
            else:
                return False
        except TypeError:
            return False

    def is_path_ok(self):
        if self.is_file_ok() and self.is_filetype_ok():
            return True
        else:
            return False
