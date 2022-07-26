import time
from chainsaw import Logger, _logger

def powertimer(fn):
    def _timing(*a, **kw):
        st = time.perf_counter()
        r = fn(*a, **kw)
        Logger(_logger()).logger.info(f"{fn.__name__} execution: {time.perf_counter() - st} seconds")
        return r
    return _timing