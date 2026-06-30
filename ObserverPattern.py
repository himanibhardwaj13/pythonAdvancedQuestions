
from abc import ABC, abstractmethod
# Observer Pattern => Notification; If we connect them with Observer then every device will be notified

class Observer:
    def update(self, msg):
        print("Notification: ", msg)
        
class Notification:
    def __init__(self):
        self.observer = []
    def attach(self, obs: Observer):
        self.observer.append(obs)
    def notify(self, msg):
        for obs in self.observer:
            obs.update(msg)
            
            
ob1,ob2= Observer(), Observer()
nfy = Notification()
nfy.attach(ob1)
nfy.attach(ob2)
nfy.notify("light is ON")
