from .chainsaw import Logger, _logger
from .powertools import powertimer

__version__ = "0.0.1"

chainsaw_logger = Logger(
    logger=_logger()
    ).logger