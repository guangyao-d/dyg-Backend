class Plugin(object):
    def __init__(self,**kwargs):
        pass

class PluginMGR:
    def __init__(self,**kwargs):
        pass
    def register(self,plugin : dict):
        plugin_obj = {}
        if "namespace" in dict:
            plugin_obj["namespace"] = plugin['namespace']
