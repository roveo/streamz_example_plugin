from streamz import Source
from tornado import gen


class from_iterable(Source):
    def __init__(self, iterable, **kwargs):
        self.iterable = iterable
        super().__init__(ensure_io_loop=True, **kwargs)

    def start(self):
        self.stopped = False
        self.loop.add_callback(self.run)

    @gen.coroutine
    def run(self):
        for i in self.iterable:
            yield self._emit(i)
