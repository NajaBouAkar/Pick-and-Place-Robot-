# Pick-and-Place-Robot
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
sudo apt install python3-wstool
```
```bash
mkdir -p ~/ws_moveit/src
cd ~/ws_moveit/src

wstool init .
wstool merge -t . https://raw.githubusercontent.com/ros-planning/moveit/master/moveit.rosinstall
wstool remove  moveit_tutorials  # this is cloned in the next section
wstool update -t .
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
