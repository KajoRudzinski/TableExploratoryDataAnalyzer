import os


class Importer:

    def __init__(self, filepath):
        self.filepath = str(filepath)
        self.file_exists = os.path.isfile(str(filepath))
