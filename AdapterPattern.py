from abc import ABC, abstractmethod
# Adapter Pattern: Creating Interface
class OldHeater:
    def heat(self):
        print("Old heatre is heating")

class NewHeaterInterface(ABC):
    @abstractmethod
    def run(self):
        pass

class NewHeaterFactory(NewHeaterInterface):
    def __init__(self, old_heater: OldHeater):
        self.old_heater = old_heater
    
    def run(self):
        self.old_heater.heat()
        
old_heater = OldHeater()
new_heater = NewHeaterFactory(old_heater)
new_heater.run()
        
