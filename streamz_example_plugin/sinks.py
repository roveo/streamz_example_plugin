from streamz import Stream
from streamz.core import _global_sinks


class sink_to_set(Stream):
    def __init__(self, upstream, target, **kwargs):
        super().__init__(upstream, **kwargs)
        self._target = target
        _global_sinks.add(self)

    def update(self, x, metadata=None, who=None):
        self._target.add(x)
