# sensor_sim.py
import json
import random
import time

def generate_sensor_data():
    data = {
        "temperature": random.randint(25, 45),
        "gas_level": random.randint(200, 700),
        "vibration": random.choice(["Normal", "High"]),
        "helmet_violations": random.randint(0, 3)  # will be replaced by main.py
    }
    return data

while True:
    data = generate_sensor_data()
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Updated sensor data:", data)
    time.sleep(5)  # update every 5 seconds
