from src.io import *


def test_ImporterObjectExists():
    assert Importer is not None


def test_GivenFilepath_ImporterChecksIfTheFileExists():
    assert Importer("empty_file.txt").file_exists
    assert not Importer("no_such_file.txt").file_exists

