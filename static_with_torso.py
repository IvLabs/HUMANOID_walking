#!/usr/bin/env python
# license removed for brevity

## Date : 12|08|2016 ##
## Author : Surabhi Verma ##
## TORSO_STATIC_WALKING ##
## INPUT FROM EXCEL SHEET, ANGLES PRECALCULATED IN MATLAB ##

import rospy
from std_msgs.msg import String
import serial
import herkulex
import time 
import xlrd
import math
herkulex.connect('/dev/ttyUSB0',115200)

#biped
l_hip_roll    = herkulex.servo(4)
l_hip_pitch   = herkulex.servo(2)
l_knee_pitch  = herkulex.servo(10)
l_ankle_pitch = herkulex.servo(5)
l_ankle_roll  = herkulex.servo(7)
r_hip_roll    = herkulex.servo(12)
r_hip_pitch   = herkulex.servo(8)
r_knee_pitch  = herkulex.servo(1)
r_ankle_pitch = herkulex.servo(11)
r_ankle_roll  = herkulex.servo(6)
#torso
#l_hand_pitch = herkulex.servo(13)
#l_hand_roll  = herkulex.servo(14)
#l_hand_yaw   = herkulex.servo(15)
#r_hand_pitch = herkulex.servo(16)
#r_hand_roll  = herkulex.servo(17)
#r_hand_yaw   = herkulex.servo(18)
## Declaration ##
s=401
angles = [[0]*10 for k in range(s)]
motor_id = [4, 2, 10, 5, 7, 12, 8, 1, 11, 6]
delay=1.5

############################
file_location = "/home/surabhi/Desktop/static_walk/static_with_torso.xlsx"
workbook = xlrd.open_workbook(file_location)
x = workbook.sheet_by_index(0)

for i in range (0, s):
 for j in range (0, 10): #0-85 86-130 131-215 215-260
 
   angles[i][j] = x.cell_value(i, j) + x.cell_value(i, j+11)
 

## MOTOR_TORQUE_ON ##

l_hip_roll.torque_on()
l_hip_pitch.torque_on()
l_knee_pitch.torque_on()
l_ankle_pitch.torque_on()
l_ankle_roll.torque_on()
r_hip_roll.torque_on()
r_hip_pitch.torque_on() 
r_knee_pitch.torque_on()
r_ankle_pitch.torque_on()
r_ankle_roll.torque_on()


def talker():

 while 1:

  for y in range (0,10): #bend
   herkulex.servo(motor_id[y]).set_servo_angle(angles[33][y],200,4) 
   time.sleep(0.0007)     
  time.sleep(2.5)

  for x in range (18,49): #shift
     for y in range (0,10):
       herkulex.servo(motor_id[y]).set_servo_angle(angles[x][y],3,4) 
       #print motor_id[y]    
       time.sleep(0.0007)
     time.sleep(0.025)

  for y in range (0,10): #swing_max
   herkulex.servo(motor_id[y]).set_servo_angle(angles[107][y],150,4)
   time.sleep(0.0007)
  time.sleep(delay)

  for y in range (0,10): #swing_min
   herkulex.servo(motor_id[y]).set_servo_angle(angles[158][y],100,4)
   time.sleep(0.0007)
  time.sleep(delay)

## second_step ##
  
  for y in range (0,10): #zero_second_step

   herkulex.servo(motor_id[y]).set_servo_angle(angles[193][y],80,4)
   time.sleep(0.0007)     
  time.sleep(0.8)

  for x in range (194,213): #shift2
     for y in range (0,10):
       herkulex.servo(motor_id[y]).set_servo_angle(angles[x][y],3,4)     
       time.sleep(0.0007)
     time.sleep(0.025)

  for y in range (0,10): #swing_max2
   herkulex.servo(motor_id[y]).set_servo_angle(angles[264][y],150,4)
   time.sleep(0.0007)     
  time.sleep(delay)
  
  for y in range (0,10): #swing_min2
   herkulex.servo(motor_id[y]).set_servo_angle(angles[313][y],150,4)
   time.sleep(0.0007)     
  time.sleep(delay)

  for y in range (0,10): #zero_second step
   herkulex.servo(motor_id[y]).set_servo_angle(angles[33][y],80,4)
   time.sleep(0.0007)     
  time.sleep(0.8)

######################
  
 herkulex.close()
if __name__ == '__main__':
    try:
       talker()
    except rospy.ROSInterruptException:
       pass


