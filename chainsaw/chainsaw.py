import time
import logging
from rich.logging import RichHandler

class Logger:
    def __init__(self, logger):
        self.logger = logger
            
def _logger(
    level="NOTSET",
    logger_blocklist=[
        "fiona",
        "rasterio",
        "matplotlib",
        "PIL",
        "wordcloud",
        "fontTools",
        "base64",
        "io",
        "scipy",
        "shapely",
        "itertools"],
    rich_tracebacks=True):

    logging.basicConfig(
            level=level, 
            format="%(message)s", 
            datefmt="[%X]", 
            handlers=[RichHandler(rich_tracebacks=rich_tracebacks)]
            )

    for module in logger_blocklist:
        logging.getLogger(module).setLevel(logging.WARNING)
            
    return logging.getLogger("rich")
