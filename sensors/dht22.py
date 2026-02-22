from datetime import datetime, timedelta
from random import gauss, uniform
from struct import pack

from core import Sensor, Env_Model

class Dht22(Sensor):
    def __init__(self,sensor_id, env_model: Env_Model, state=True, bin=False):
        super().__init__(sensor_id,state)
        self.env_model = env_model
        self.bin = bin
        now = datetime.now()
        self.last_access = now
        self.last_temp = self.env_model.get_env_temp(now)
        self.last_hum = self.env_model.get_env_hum(self.last_temp)

    def add_temp_noise_and_relaxation(self, envtemp):
        #getting noise
        noise = gauss(0,0.1)
        #defining a random step
        k = uniform(0.05,0.1)
        step = k*(envtemp - self.last_temp)
        #getting temp + inertia + noise
        self.last_temp = self.last_temp + step + noise
        return self.last_temp

    def add_hum_noise_and_relaxation(self, env_hum):
        noise = gauss(0,0.5) #Very High Noise!
        k = uniform(0.05,0.1)
        step = k * (env_hum - self.last_hum)
        self.last_hum = self.last_hum + step + noise
        return self.last_hum

    def read_sensor(self):
        now = datetime.now()
        if now < self.last_access + timedelta(seconds=2):
            print(f'Sensor {self.sensor_id} hasn\'t updated yet. Min interval 2 sec.')
            return
        self.env_model.update_env(now)
        updated_temp = self.add_temp_noise_and_relaxation(self.env_model.env_temp)
        updated_hum = self.add_hum_noise_and_relaxation(self.env_model.env_hum)        
        temp = max(-40.0, min(80.0, updated_temp))
        hum = max(0.0, min(100.0, updated_hum))
        self.last_access = now
        return {
            "sensor_id": self.sensor_id,
            "temp": self.convert_to_bin(temp) if self.bin else round(temp, 1),
            "hum": self.convert_to_bin(hum) if self.bin else round(hum, 1),
            "timestamp": now.strftime("%H:%M:%S")
        }
    
    def convert_to_bin(self, float_data):
        value = int(abs(float_data)*10)
        if float_data<0:
            value |= 0x8000
            return pack('>H',value)
        return pack('>H',value)
    
    def __repr__(self):
        return (f"Dht22(id='{self.sensor_id}', "
                f"state={self.state}, "
                f"mode={'Binary' if self.bin else 'Decimal'}, "
                f"last_temp={round(self.last_temp, 1)}°C, "
                f"last_hum={round(self.last_hum, 1)}%, "
                f"season={self.env_model.season.name})")
    
    def __str__(self):
        status = "Active" if self.state else "Inactive"
        b_temp = ' '.join(f'{b:08b}' for b in self.convert_to_bin(self.last_temp))
        b_hum =  ' '.join(f'{b:08b}' for b in self.convert_to_bin(self.last_hum))
        t_display = f"{self.last_temp:.1f}°C" if not self.bin else f"{b_temp}"
        h_display = f"{self.last_hum:.1f}%" if not self.bin else f"{b_hum}"
        return (f"--- Sensor {self.__class__.__name__} [{self.sensor_id}] ---\n"
                f"Status: {status}\n"
                f"Temperature: {t_display}\n"
                f"Humidity: {h_display}\n"
                f"Season: {self.env_model.season.name}\n"
                f"------------------------------")