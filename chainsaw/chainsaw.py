import time
import logging
from rich.logging import RichHandler

class Logger:
    level = "NOTSET"
    logging.basicConfig(
            level=level, 
            format="%(message)s", 
            datefmt="[%X]", 
            handlers=[RichHandler()]
            )
    logger = logging.getLogger("rich")
    def __init__(self, level, logger):
        self.level = level
        self.logger = logger


def benchmark(fn):
    def _timing(*a, **kw):
        st = time.perf_counter()
        r = fn(*a, **kw)
        Logger.logger.info(f"{fn.__name__} execution: {time.perf_counter() - st} seconds")
        return r
    return _timing
