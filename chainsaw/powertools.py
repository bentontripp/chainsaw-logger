import time, functools, operator
from chainsaw import Logger, _logger

# Timing decorator
def powertimer(fn):
    def _timing(*a, **kw):
        st = time.perf_counter()
        r = fn(*a, **kw)
        Logger(_logger()).logger.info(f"{fn.__name__} execution: {time.perf_counter() - st} seconds")
        return r
    return _timing

# Flatten nested lists
def powerhammer(nl):
    return functools.reduce(operator.iconcat, nl, [])