cmake_minimum_required(VERSION 2.8.3)
project(beast)

find_package(catkin REQUIRED COMPONENTS
  beast_msgs
  beast_srvs
  rospy
)
catkin_python_setup()
catkin_package()

# install(PROGRAMS
#   scripts/my_python_script
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )