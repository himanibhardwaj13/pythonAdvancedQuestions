from abc import ABC, abstractmethod
# Singleton Pattern: Creating one instance enforced
class configManager:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance=super().__new__(cls)
            cls._instance.settings={}
        return cls._instance
        
config1, config2= configManager(), configManager()
config1.settings["theme"]="dark"
print("single class instance ", config1 is config2)
        
