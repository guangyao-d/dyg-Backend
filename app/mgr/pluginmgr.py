import logging
import os

module_logger = logging.getLogger("pluginmgr")

class Plugin(object):
    def __init__(self,namespace="BasicPythonPlugin"):
        self.namespace = namespace
        self.logger = logging.getLogger(self.namespace)
        self.logger.debug("Loading Plugin %s.".format(self.namespace))
        return
    def registerHandler(self):
        pass

class PluginMGR:
    def __init__(self):
        self.logger = logging.getLogger("PluginMGR")
        self.logger.info("Loading...")
        self.loaded_plugins = []
        if not 'plugins' in os.listdir("."):
            os.mkdir("plugins")
        plugins = os.listdir("./plugins")
        for item in plugins:
            if os.path.isfile(os.path.abspath("./plugins/"+item)):
                self.loaded_plugins.append(__import__(os.path.abspath("./plugins/"+item)))


    def register(self):
        os.path.get()