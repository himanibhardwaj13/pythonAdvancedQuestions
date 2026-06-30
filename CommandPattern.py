from abc import ABC, abstractmethod
# Command Pattern: Encapsulate user actions
class Command:
    def __init__(self, action):
        self.action=action
    def execute(self):
        self.action()

def turn_light_on():
    print("Light is ON")
    
def turn_light_off():
    print("Light is OFF")
    
on_cmd = Command(turn_light_on)
off_cmd = Command(turn_light_off)
on_cmd.execute()
off_cmd.execute()
        
