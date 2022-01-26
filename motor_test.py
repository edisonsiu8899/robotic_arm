import time
from adafruit_motorkit import MotorKit

kit = MotorKit()
print("Printed: ", str(kit))

for i in range(100):
    kit.stepper1.onestep()