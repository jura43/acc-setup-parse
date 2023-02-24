from accsetupparse import McLaren720S
import json

f = open("test.json")
data = json.load(f)
f.close()

car = McLaren720S(data)

print(car.steeringRatio)