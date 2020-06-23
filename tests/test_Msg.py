from src import Msg


def test_MsgWhenApplicationStarts():
    assert Msg.start() == "\nTEDA started"


def test_MsgWhenApplicationEnds():
    assert Msg.end() == "\nTEDA closed"
