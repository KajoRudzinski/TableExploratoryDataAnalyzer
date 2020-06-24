from src import msg


def test_MsgWhenApplicationStarts():
    assert msg.start() == "\nTEDA started"


def test_MsgWhenApplicationEnds():
    assert msg.end() == "\nTEDA closed"
