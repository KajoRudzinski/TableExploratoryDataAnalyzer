from src import msg


def test_start_app_msg():
    assert msg.start_app_msg() == "\nTEDA started"


def test_close_app_msg():
    assert msg.close_app_msg() == "\nTEDA closed"


def test_get_app_name():
    assert msg.get_app_name() == "Table Exploratory Data Analysis"


def test_format_ok_status():
    assert msg.format_status("test") == "Status [OK]: test"


def test_format_error_status():
    assert msg.format_status("test", error=True) == "Status [ERROR]: test"
