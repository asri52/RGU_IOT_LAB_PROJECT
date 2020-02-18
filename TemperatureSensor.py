from Sensor import Sensor

class TemperatureSensor(Sensor):

    id = None
    def _init_(self, id):
        self.id = id
    def getReading(self):
        return -1
