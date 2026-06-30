#factory Pattern
from abc import ABC, abstractmethod
class Device(ABC):
    @abstractmethod
    def operate(self):
        pass

class Thermostat(Device):
    def operate(self):
        print("Thermostat set to 22C")

class Light(Device):
    def operate(self):
        print("Light is on.")

class Door(Device):
    def operate(self):
        print("Door is locked")
        
class DeviceFactory:
    @staticmethod
    def create_device(device_type):
        if device_type == "light":
            return Light()
        elif device_type == "thermostat":
            return Thermostat()
        elif device_type == "door":
            return Door()
        else:
            raise ValueError("Unknow Device")
            
class EnergyStrategy(ABC):
    @abstractmethod
    def apply(self):
        pass

class NormalMode(EnergyStrategy):
    def apply(self):
        print("Normal mode ON")
        
class EcoMode(EnergyStrategy):
    def apply(self):
        print("ECO mode ON")
        
class SmartHome:
    def __init__(self, strategy:EnergyStrategy):
        self.strategy = strategy
    def run(self):
        self.strategy.apply()
        

class Observe:
    def update(self, msg):
        print("Notification: ", msg)
        
class Notifications:
    def __init__(self):
        self.observers = []
    def attach(self, obs: Observe):
        self.observers.append(obs)
    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)
        
class OldHeater:
    def heat(self):
        print("old heater warming")
        
class HeaterInterface:
    def start(self):
        pass
    
class NewHeater(HeaterInterface):
    def __init__(self, old_heater):
        self.old_heater = old_heater 
    def start(self):
        self.old_heater.heat()
        
device = DeviceFactory.create_device('light')
device.operate()
    
selectmode = SmartHome(EcoMode())
selectmode.run()

notification = Notifications()
ob1, ob2 = Observe(), Observe()
notification.attach(ob1)
notification.attach(ob2)
notification.notify("Light Switch ON")

old_heater = OldHeater()
new_heater = NewHeater(old_heater)
new_heater.start()
