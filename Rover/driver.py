from robot import Robot
import time
 
try:
    r=Robot()
    r.xboxControl()
except Exception as e:
    print(e)
finally:
    r.motor.stop()