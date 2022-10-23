import logging
import sys
def InitLog(is_Debug=False):
    global logger
    logger = logging.getLogger("main")
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("app.log",maxBytes = 1*1024,backupCount = 3)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('(%(levelname)s)[%(asctime)s][%(name)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    console = logging.StreamHandler()
    console.setLevel(logging.WARN)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.debug("Successfully Initialed Logger.")

if __name__ == "__main__":
    InitLog