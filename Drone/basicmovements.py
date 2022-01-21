from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 0, 25, 0)
sleep(4)
me.send_rc_control(0, 0, -25, 0)
sleep(3)
me.send_rc_control(0, 0, 0, 0)
me.land()