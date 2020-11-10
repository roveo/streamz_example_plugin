from streamz import Stream


class repeat(Stream):
    def __init__(self, n):
        self.n = n

    def update(self, x, metadata=None, who=None):
        for _ in range(self.n):
            self._emit(x, metadata=metadata, who=who)
