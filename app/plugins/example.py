from app.mgr.pluginmgr import Plugin


class Example(Plugin):
    def __init__(self):
        super().__init__("ExamplePlugin")
plugin_info = {
    "mainClass":Example,
    "register":{
        "handler":["/","/example"]
    }
}