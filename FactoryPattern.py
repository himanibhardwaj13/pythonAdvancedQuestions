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
        
device = DeviceFactory.create_device('light')
device.operate()
