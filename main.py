from datetime import datetime
from core import Env_Model, Season
from sensors import Dht22           

def main():
    mundo = Env_Model(Season.month(datetime.now().month))
    sensor = Dht22("SALA_01", mundo)
    
    print(f"DigitalTwin Basic v0.1 iniciado.")
    print(sensor)

if __name__ == "__main__":
    main()