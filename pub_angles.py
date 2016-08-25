#!/usr/bin/env python
# license removed for brevity

from beginner_tutorials.msg import angles_msg
import rospy
import serial
import herkulex
import time 
herkulex.connect('/dev/ttyUSB0',115200)

x = herkulex.servo(20)
y = herkulex.servo(19)

angles=[20,19]

## MOTOR_TORQUE_ON ##

x.torque_on()
y.torque_on()

angles_arr=['pitch','yaw']
timer=time.time()
delay=1.5*60

def pub_angles():

 pub = rospy.Publisher('angles_topic',angles_msg,queue_size=10) #node is publishing on the topic, angles_topic 
 rospy.init_node('pub_angles', anonymous=True) #pub_angles is the name of the publishing node
 
 rate = rospy.Rate(50) # 40hz
 msg = angles_msg()

 x.set_servo_angle(10,200,4)
 time.sleep(0.007)
 y.set_servo_angle(10,200,4)
 time.sleep(0.007)

 while not rospy.is_shutdown():
  print "b"
  while time.time() < (timer + delay):
    #if time.time() < (timer + delay):
     #break
    msg.pitch = herkulex.servo(20).get_servo_angle()
    time.sleep(0.0014)
    print "a"
    msg.yaw = herkulex.servo(19).get_servo_angle()
    time.sleep(0.0014)
    rospy.loginfo(msg)
    print "c"
    pub.publish(msg)   
    #10ms #100Hz
  herkulex.close()
   
if __name__ == '__main__':
    try:
       pub_angles()
    except rospy.ROSInterruptException:
       pass
