from src import msg


def test_internal_msg_app_starts():
    assert msg.start_app_msg() == "\nTEDA started"


def test_internal_msg_app_closes():
    assert msg.close_app_msg() == "\nTEDA closed"
