import os
import logging

log_path    = os.path.join(os.getcwd(), "neko.log")
logger      = logging.getLogger("Neko")
handler     = logging.FileHandler(log_path)
formatter   = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s")

handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

