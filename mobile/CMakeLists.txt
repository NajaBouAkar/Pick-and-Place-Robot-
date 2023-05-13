cmake_minimum_required(VERSION 2.8.3)

project(mobile)

find_package(catkin REQUIRED COMPONENTS
  gazebo
  rospy
  roscpp
  std_msgs
  rviz
  message_generation
  tf
  cv_bridge
  urdf
  image_transport
  xacro
  sensor_msgs
  geometry_msgs
  controller_interface
  hardware_interface
  pluginlib
)

catkin_package(CATKIN_DEPENDS
     geometry_msgs
     roscpp
     rospy
     std_msgs
)

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
