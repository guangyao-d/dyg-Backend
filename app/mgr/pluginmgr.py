import logging
import os

module_logger = logging.getLogger("pluginmgr")

class Plugin(object):
    def __init__(self,namespace="BasicPythonPlugin"):
        self.namespace = namespace
        self.logger = logging.getLogger(self.namespace)
        self.logger.debug("Loading Plugin %s.".format(self.namespace))
        return
    def registerHandler(self,)

class PluginMGR:
    def __init__(self):
        self.logger = logging.getLogger("PluginMGR")
        self.logger.info("Loading...")

    def register(self):
        os.path.get()