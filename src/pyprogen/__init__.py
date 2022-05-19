"""Init module of the pyprogen package"""

import coloredlogs

__version__ = "0.0.0"

coloredlogs.install("DEBUG", fmt="%(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s")
