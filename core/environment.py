from datetime import datetime, timedelta
import math
from random import gauss, uniform
from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class Season_constants:
    average: float
    range: float
    phase: float

class Season(Enum):
    SUMMER = Season_constants(30.0, 8.0, 7.0)
    FALL = Season_constants(24.0, 10.0, 7.0)
    WINTER = Season_constants(18.0, 12.0, 6.0)
    SPRING = Season_constants(26.0, 8.0, 7.0)

    @classmethod
    def month(cls, month: int):
        map = {
            12: cls.SUMMER, 1: cls.SUMMER, 2: cls.SUMMER,
            3: cls.FALL, 4: cls.FALL, 5: cls.FALL,
            6: cls.WINTER, 7: cls.WINTER, 8: cls.WINTER,
            9: cls.SPRING, 10: cls.SPRING, 11: cls.SPRING
        }
        return map.get(month, cls.SUMMER)

class Env_Model:
    def __init__(self, season: Season):
        self.season = season
        self.update_env(datetime.now())

    def get_env_temp(self, now: datetime):
        hour_decimals = now.hour+(now.minute/60)
        return  self.season.value.average + self.season.value.range * math.sin(((2*math.pi)/24)*(hour_decimals-self.season.value.phase))
        
    def get_env_hum(self, temp):
        return 100-(temp*1.3)
    
    def update_env(self, now: datetime):
            self.env_temp = self.get_env_temp(now)
            self.env_hum = self.get_env_hum(self.env_temp)