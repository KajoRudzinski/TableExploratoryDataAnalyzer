from src import msg_formats_graphics


def test_MsgWhenApplicationStarts():
    assert msg_formats_graphics.start() == "\nTEDA started"


def test_MsgWhenApplicationEnds():
    assert msg_formats_graphics.end() == "\nTEDA closed"
