# Pick-and-Place-Robot-
Pick and Place robot simulation on ROS using plugins and controllers.

# Installation
Our project is divided into three packages final_project, mobile, and moveit_mobilerobot.
To be able to use these packages you have to install the follwing line of codes.
Controller:
```bash
sudo apt-get install ros-noetic-controller-manager
```
```bash
sudo apt-get install ros-noetic-ros-control ros-noetic-ros-controllers
```
Moveit:
```bash

```

# Commands

to be able to run the project you have to run the command in this following order.
1- to launch Gazebo and the controllers
```bash
roslaunch mobile robot_urdf.launch
```
2- To launch rviz
```bash
roslaunch mobile display.launch
```
3- Python scripts
```bash
rosrun final_project key.py
```
Before running the below command you have to make sure to enable the camera on your Virtual machine
```bash
rosrun final_project camera_node.py
```
```bash
rosrun final_project arm_controller.py
```
