import random

class Sensor:
    id = None
    def _init_(self,id):
        self.id = id
    def getReading(self):
        return random.random()
