import Sensor from Sensor as s
import TemperatureSensor from TemperatureSensor as ts

class HomeHub:
    sensors = list[]
    def _init_(self, id):
        sensor = s.Sensor("sensor1")
        tSensor = ts.TemperatureSensor("tSensor")
        sensors.append(sensor)
        sensors.append(tSensor)
        
    
