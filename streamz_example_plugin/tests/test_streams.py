import time

from streamz import Stream


def test_from_iterable():
    stream = Stream.from_iterable(range(10))
    L = stream.sink_to_list()

    stream.start()

    time.sleep(0.01)

    assert L == list(range(10))


def test_repeat():
    stream = Stream.from_iterable(range(2)).repeat(2)
    L = stream.sink_to_list()

    assert L == [0, 0, 1, 1]