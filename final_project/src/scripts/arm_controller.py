#!/usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import random
from final_project.msg import hand
from sensor_msgs.msg import JointState

griper1_j_incr=0.0
griper2_j_incr=0.0
thumb = False
first_finger= False
second_finger=False
third_finger=False
fourth_finger=False


def ss_callback(msg):
   global thumb, first_finger, second_finger, third_finger, fourth_finger
   thumb= msg.thumb
   first_finger=msg.firstfinger
   second_finger=msg.secondfinger
   third_finger=msg.thirdfinger
   fourth_finger=msg.fourthfinger


def publisher_controller():
    global griper1_j_incr,griper2_j_incr,link1_j_increment,link2_j_increment,link3_j_increment,link4_j_increment,link5_j_increment
    #control part
    rospy.init_node('node_controller', anonymous=True)

    pub = rospy.Publisher('/robot_arm_controller/command', JointTrajectory, queue_size=10)
    pub2 = rospy.Publisher('/hand_ee_controller/command', JointTrajectory, queue_size=10)
    rospy.Subscriber('hand_fingers', hand, ss_callback)
    
    

    while not rospy.is_shutdown():
     #This is the Ideal case:
     
     if thumb==True and first_finger==True and second_finger==True and third_finger==True and fourth_finger==True:
      msg=JointTrajectory()

      msg.header.stamp=rospy.Time.now()
      msg.header.frame_id=''
      msg.joint_names=['link1_j','link2_j','link3_j','link4_j','link5_j']

      point=JointTrajectoryPoint()
      point.positions= [0.0,0.0,0.0,0.0,0.0]
      point.velocities=[0.001,0.001,0.001,0.001,0.001]
      point.accelerations=[]
      point.effort=[]

      msg.points.append(point)

      point.time_from_start=rospy.Duration(1)

      pub.publish(msg)

      rospy.loginfo(msg)
      #This is the pickup case for the arm
     elif thumb==True and first_finger==False and second_finger==False and third_finger==False and fourth_finger==False:
      msg=JointTrajectory()

      msg.header.stamp=rospy.Time.now()
      msg.header.frame_id=''
      msg.joint_names=['link1_j','link2_j','link3_j','link4_j','link5_j']

      point=JointTrajectoryPoint()

      point.positions= [0.0,1.982,1.65,0.0,0.0]
      point.velocities=[0.02,0.02,0.02,0.02,0.02]
      point.accelerations=[]
      point.effort=[]

      msg.points.append(point)

      point.time_from_start=rospy.Duration(1)

      pub.publish(msg)

      rospy.loginfo(msg)  
      #This is the opposite of pickup case for the arm
     elif thumb==False and first_finger==True and second_finger==True and third_finger==True and fourth_finger==True:
      msg=JointTrajectory()

      msg.header.stamp=rospy.Time.now()
      msg.header.frame_id=''
      msg.joint_names=['link1_j','link2_j','link3_j','link4_j','link5_j']

      point=JointTrajectoryPoint()

      point.positions= [3.095,1.982,1.65,0.0,0.0]
      point.velocities=[0.02,0.02,0.02,0.02,0.02]
      point.accelerations=[]
      point.effort=[]

      msg.points.append(point)

      point.time_from_start=rospy.Duration(1)

      pub.publish(msg)

      rospy.loginfo(msg)   
      #This is the Take up case for the arm 
     elif first_finger==True and second_finger==False and thumb==False and third_finger==False and fourth_finger==False:
      
      msg=JointTrajectory()
      msg.header.stamp=rospy.Time.now()
      msg.header.frame_id=''
      msg.joint_names=['link1_j','link2_j','link3_j','link4_j','link5_j']

      point=JointTrajectoryPoint()

      point.positions= [0.0,-0.3472,-0.4303,0.0,0.0]
      point.velocities=[0.02,0.02,0.02,0.02,0.02]
      point.accelerations=[]
      point.effort=[]

      msg.points.append(point)

      point.time_from_start=rospy.Duration(1)

      pub.publish(msg)

      rospy.loginfo(msg)  
     #This is the opposite of Take up case for the arm 
     elif first_finger==False and second_finger==True and thumb==True and third_finger==True and fourth_finger==True:
      
      msg=JointTrajectory()
      msg.header.stamp=rospy.Time.now()
      msg.header.frame_id=''
      msg.joint_names=['link1_j','link2_j','link3_j','link4_j','link5_j']

      point=JointTrajectoryPoint()

      point.positions= [3.0905,-0.3472,-0.4303,0.0,0.0]
      point.velocities=[0.02,0.02,0.02,0.02,0.02]
      point.accelerations=[]
      point.effort=[]

      msg.points.append(point)

      point.time_from_start=rospy.Duration(1)

      pub.publish(msg)

      rospy.loginfo(msg)  
     #This is the Place case for the arm 
     elif first_finger==False and second_finger==True and thumb==False and third_finger==False and fourth_finger==False:
      
      msg=JointTrajectory()
      msg.header.stamp=rospy.Time.now()
      msg.header.frame_id=''
      msg.joint_names=['link1_j','link2_j','link3_j','link4_j','link5_j']

      point=JointTrajectoryPoint()

      point.positions= [0.0,1.2831,0.597,0.0,0.0]
      point.velocities=[0.02,0.02,0.02,0.02,0.02]
      point.accelerations=[]
      point.effort=[]

      msg.points.append(point)

      point.time_from_start=rospy.Duration(1)

      pub.publish(msg)

      rospy.loginfo(msg)  
    #This is the opposite of Place case for the arm 
     elif first_finger==True and second_finger==False and thumb==True and third_finger==True and fourth_finger==True:
      
      msg=JointTrajectory()
      msg.header.stamp=rospy.Time.now()
      msg.header.frame_id=''
      msg.joint_names=['link1_j','link2_j','link3_j','link4_j','link5_j']

      point=JointTrajectoryPoint()

      point.positions= [3.0905,1.2831,0.597,0.0,0.0]
      point.velocities=[0.02,0.02,0.02,0.02,0.02]
      point.accelerations=[]
      point.effort=[]

      msg.points.append(point)

      point.time_from_start=rospy.Duration(1)

      pub.publish(msg)

      rospy.loginfo(msg)   
     #This is the closed gripper case to pick up an object
     elif first_finger==False and second_finger==False and thumb==False and third_finger==False and fourth_finger==True:
      
      msg=JointTrajectory()
      msg.header.stamp=rospy.Time.now()
      msg.header.frame_id=''
      msg.joint_names=['grip1_j','grip2_j']

      point=JointTrajectoryPoint()

      point.positions= [-0.05,0.05]
      point.velocities=[0.02,0.02]
      point.accelerations=[]
      point.effort=[]

      msg.points.append(point)

      point.time_from_start=rospy.Duration(1)

      pub2.publish(msg)

      rospy.loginfo(msg)   
    #This is the opened gripper case to pick up an object
     elif first_finger==True and second_finger==False and thumb==False and third_finger==False and fourth_finger==True:
      
      msg=JointTrajectory()
      msg.header.stamp=rospy.Time.now()
      msg.header.frame_id=''
      msg.joint_names=['grip1_j','grip2_j']

      point=JointTrajectoryPoint()

      point.positions= [0.00,0.00]
      point.velocities=[0.02,0.02]
      point.accelerations=[]
      point.effort=[]

      msg.points.append(point)

      point.time_from_start=rospy.Duration(1)

      pub2.publish(msg)

      rospy.loginfo(msg)     
  
  
  






if __name__ == '__main__':
    try:
        publisher_controller()
    except rospy.ROSInterruptException:
        pass    