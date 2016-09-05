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

s=50

angles = [[0]*10 for k in range(s)]
############################
file_location = "/home/shalini/Desktop/static_with_torso.xlsx"
workbook = xlrd.open_workbook(file_location)
x = workbook.sheet_by_index(0)
for i in range (0, s):
 for j in range (0, 10): #0-85 86-130 131-215 215-260
 
   angles[i][j] = x.cell_value(i, j) + x.cell_value(i, j+11)
 

def talker():

    while not rospy.is_shutdown():
     pub = rospy.Publisher('angles',angle_array, queue_size=10) #node is publishing to the angles topic 
     rospy.init_node('test_array', anonymous=True) #plot_graphs is the name of the publishing node
     t_init = time.clock()
     msg1=angle_array()
     msg2=angle_array()
     rate = rospy.Rate(40) # 40hz
     for y in range(0,10):
         msg1.ang[y]= angles[0][y]
         time.sleep(0.0014)
     pub.publish(msg1.ang[y])
     rospy.loginfo(msg1.ang[y])

if __name__ == '__main__':
    try:
       talker()
    except rospy.ROSInterruptException:
       pass



