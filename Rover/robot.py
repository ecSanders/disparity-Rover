import xbox
import math
import time

def moveByAxis(self, x, y):     
    if x == 0.0 and y == 0.0:
        # nowhere to move, stop
        self.motor.stop()
    elif x == 0:
        # only forward / backward
        if y < 0:
            self.motor.backward()
        else:
            self.motor.forward()
    else:
        angle = math.degrees(math.atan(y/x))
        angle += 180 if x < 0 else 360
        angle = angle % 360
        
        if angle == 0:
            self.motor.forwardRight()
        elif angle == 180:
            self.motor.forwardLeft()
        if angle > 0 and angle < 90:
            # forwardRight
            self.motor.forwardRight()
            time.sleep(self.motor.SEC_PER_TURN / 360.0 * angle)
            self.motor.forward()
            time.sleep(5.0 / self.motor.DIST_PER_SEC) # move 5cm forward
        elif angle > 90 and angle < 180:
            # forwardLeft
            angle -= 90
            self.motor.forwardLeft()
            time.sleep(self.motor.SEC_PER_TURN / 360.0 * angle)
            self.motor.forward()
            time.sleep(5.0 / self.motor.DIST_PER_SEC) # move 5cm forward

def xboxControl(self):
    joy = xbox.Joystick()
    while not joy.Back():
    
        
        # button A to stop
        if joy.A():
            self.motor.stop()
        else:
            # left joystick to move
            x, y = joy.leftStick()
            self.moveByAxis(x, y)
                
    joy.close()


"""
sudo xboxdrv --detach-kernel-driver
ctrl + C
"""