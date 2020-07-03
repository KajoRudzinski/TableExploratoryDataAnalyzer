import numpy as np
import os


class FileReader:
    def __init__(self, path=None):
        self.path = path
        self.accepted_filetypes = "csv", "txt"
        self.path_is_accepted = self.is_path_ok()
        self.data = None
        self.error = False

    def read(self):
        if self.path_is_accepted:
            self._get_data()
        else:
            self.error = True

    def _get_data(self):
        try:
            self.data = np.genfromtxt(self.path)
        except:
            self.error = True

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