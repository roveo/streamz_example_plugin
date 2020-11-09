import time

import streamz_plugin  # noqa: F401
from streamz import Stream


def test_from_iterable():
    stream = Stream.from_iterable(range(10))
    L = stream.sink_to_list()

    stream.start()

    time.sleep(0.01)

    assert L == list(range(10))
