import time
import logging
from rich.logging import RichHandler

class Chainsaw:
    def logger(self, level="NOTSET"):
        self.level = level
        logging.basicConfig(
            level=level, format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])  
            # set level=20 or logging.INFO to turn off debug
        return logging.getLogger("rich")

    def benchmark(self, fn):
        def _timing(*a, **kw):
            st = time.perf_counter()
            r = fn(*a, **kw)
            self.logger.info(f"{fn.__name__} execution: {time.perf_counter() - st} seconds")
            return r
        return _timing
