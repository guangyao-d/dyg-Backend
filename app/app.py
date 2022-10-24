import logging
import os
import sys
from mgr.pluginmgr import PluginMGR
def InitLog(is_Debug=False):
    global logger
    logger = logging.getLogger("main")
    lvl_log = logging.INFO
    lvl_cons = logging.WARN
    if is_Debug:
        lvl_log = logging.DEBUG
        lvl_cons = logging.DEBUG
    logger.setLevel(level = lvl_log)
    if not 'logs' in os.listdir("."):
            os.mkdir("logs")
    handler = logging.FileHandler("./logs/app.log")
    handler.setLevel(lvl_log)
    formatter = logging.Formatter('(%(levelname)s)[%(asctime)s][%(name)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    console = logging.StreamHandler()
    console.setLevel(lvl_cons)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.debug("Successfully Initialed Logger.")

if __name__ == "__main__":
    InitLog(is_Debug=True)
    Plugins = PluginMGR()