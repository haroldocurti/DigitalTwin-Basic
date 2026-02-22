class Sensor:
    def __init__(self,sensor_id, state=True):
        self.sensor_id = sensor_id
        self.state = state
    def read_sensor(self):
        ...        