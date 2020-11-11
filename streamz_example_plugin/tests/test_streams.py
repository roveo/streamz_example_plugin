import time

from streamz import Stream


def test_from_iterable():
    stream = Stream.from_iterable(range(10))
    L = stream.sink_to_list()
    stream.start()
    time.sleep(0.01)

    assert L == list(range(10))


def test_repeat():
    source = Stream()
    L = source.repeat(2).sink_to_list()
    time.sleep(0.01)

    for i in range(2):
        source.emit(i)

    assert L == [0, 0, 1, 1]


def test_sink_to_set():
    source = Stream()
    S = set()
    source.repeat(2).sink_to_set(S)

    for i in range(2):
        source.emit(i)

    assert S == set([0, 1])
