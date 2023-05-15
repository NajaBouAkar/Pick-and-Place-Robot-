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
For the camer_hand.py code you need to download the hand tracking modules and opencv library.
To be able to run SLAM you have to install the following
```bash
sudo apt-get install ros-noetic-slam-gmapping
```

# Commands

To be able to run the project you have to run these commands in this following order.
1- to launch Gazebo and the controllers
```bash
roslaunch mobile robot_urdf.launch
```
2- To launch rviz
```bash
roslaunch mobile display.launch
```
3- Python scripts
This code runs the teleop keys code to move the robot.
```bash
rosrun final_project key.py
```
This code runs opens the camera in order to read the finger states and before running the below command you have to make sure to enable the camera on your Virtual machine. The results are published to a hand.msg file.
```bash
rosrun final_project camera_node.py
```
This code runs a node to control the ar from values read from the hand.msg
```bash
rosrun final_project arm_controller.py
```
4- SLAM

  1- to launch Gazebo and the controllers
  ```bash
  roslaunch mobile robot_urdf.launch
  ```
  2- To launch rviz
  Also make sure to add the robot model and to set the frame to be base_link. And to add the laserscan and the images. In addition make sure to add the topics of both laserscan and image. 
  ```bash
  roslaunch mobile display.launch
  ```
  3- Run gmapping 
  ```bash
  rosrun gmapping slam_gmapping scan:=/mobile/laser/scan
  ```
  4- Run the teleop keys code
  ```bash
  rosrun final_project key.py
  ```
  5- Save the map
  ```bash
  rosrun map_server map_saver -f ~/<map_name>
  ```
5- Moveit
To control the arm using the moveit package run the following command
```bash
rsolaunch moveit_mobilerobot full_robot_arm.launch
```

