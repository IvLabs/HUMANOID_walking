#!/usr/bin/env python
# license removed for brevity
## Author :Addepalli Shalini
## Date : 4|09|2016 ##
## INPUT FROM EXCEL SHEET, ANGLES PRECALCULATED IN MATLAB ##
import rospy
from std_msgs.msg import Float64
from  beginner_tutorials.msg import angle_array
import serial
import herkulex
import time 
import xlrd
import math


herkulex.connect('/dev/ttyUSB0',115200)

#biped
l_hip_roll    = herkulex.servo(19)
l_hip_pitch   = herkulex.servo(20)
s=50

angles = [[0]*10 for k in range(s)]

############################
file_location = "/home/shalini/Desktop/static_with_torso.xlsx"
workbook = xlrd.open_workbook(file_location)
x = workbook.sheet_by_index(0)
for i in range (0, s):
 for j in range (0, 10): #0-85 86-130 131-215 215-260
 
   angles[i][j] = x.cell_value(i, j) + x.cell_value(i, j+11)
 
deg=[]
## MOTOR_TORQUE_ON ##
l_hip_roll.torque_on()
l_hip_pitch.torque_on()


def talker():
      
    pub = rospy.Publisher('angles', Float64 , queue_size=10) #node is publishing to the angles topic 
    rospy.init_node('test_2motors', anonymous=True) #plot_graphs is the name of the publishing node
    msg1=angle_array()
    rate = rospy.Rate(40) # 40hz
    while not rospy.is_shutdown():
     for j in range (0,1):
      for y in range (0,2): #bend
         herkulex.servo(motor_id[y]).set_servo_angle(angles[33][y],200,4) 
         time.sleep(0.0007)   
      delay=2.5
      begin= time.time()
      while  ((time.time()-begin) < delay):
        for y in range(0,2):
         deg.append( herkulex.servo(motor_id[y]).get_servo_angle())
         rospy.loginfo(type(deg[y]))
         time.sleep(0.0014)
         pub.publish(deg[y])
         rospy.loginfo(deg[y])


if __name__ == '__main__':
    try:
       talker()
    except rospy.ROSInterruptException:
       pass



