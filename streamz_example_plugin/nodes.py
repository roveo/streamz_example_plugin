from streamz import Stream
from tornado import gen


class repeat(Stream):
    def __init__(self, upstream, n, **kwargs):
        super().__init__(upstream, **kwargs)
        self.n = n

    @gen.coroutine
    def update(self, x, metadata=None, who=None):
        for _ in range(self.n):
            yield self._emit(x, metadata=metadata, who=who)
