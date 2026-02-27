from core import Env_Model
from sensors import Dht22
from struct import pack

class Dht11(Dht22):
    def __init__(self,sensor_id, env_model: Env_Model,min_temp=0.0, max_temp=50.0, state=True, bin=False):
        super().__init__(sensor_id, env_model, min_temp=min_temp, max_temp=max_temp, state=state, bin=bin)
          
    def convert_to_bin(self, float_data):
        value = int(abs(float_data)*10)
        return pack('>H',value)
    