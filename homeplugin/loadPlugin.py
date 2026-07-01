import importlib

class LoadPlugins:
    @staticmethod
    def load_plugin(plugin_name):
        module_name = f"plugins.{plugin_name}"
        module = importlib.import_module(module_name)
        for name in dir(module):
            attr = getattr(module, name)
            if isinstance(attr, type) and issubclass(attr, module.Plugin) and attr is not module.Plugin:
                return attr()
