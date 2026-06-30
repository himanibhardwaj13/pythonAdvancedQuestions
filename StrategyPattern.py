from abc import ABC, abstractmethod
# Strategy Pattern: Swap the algorithms interchangable
class EngeryStrategy(ABC):
    @abstractmethod
    def start(self):
        pass
class NormalMode(EngeryStrategy):
    def start(self):
        print("Normal Mode is all set.")
        
class EcoMode(EngeryStrategy):
    def start(self):
        print("ECO Mode is all set.")
        
class ThermoStat:
    def __init__(self, strategy: EngeryStrategy):
        self.strategy = strategy
        
    def run(self):
        self.strategy.start()
        
thermo = ThermoStat(EcoMode())
thermo.run()
