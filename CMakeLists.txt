cmake_minimum_required(VERSION 3.0.2)
project(r3live_tools)

find_package(catkin REQUIRED COMPONENTS livox_camera_calib livox_ros_driver)

file(
  MAKE_DIRECTORY
  calib/images
  calib/pcds
  bags
)
###################################
## catkin specific configuration ##
###################################
catkin_package(
  #  INCLUDE_DIRS include
  #  LIBRARIES r3live_tools
  #  CATKIN_DEPENDS livox_camera_calib livox_ros_driver
  #  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  # include
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
# catkin_install_python(PROGRAMS
#   scripts/my_python_script
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark executables for installation
## See http://docs.ros.org/melodic/api/catkin/html/howto/format1/building_executables.html
# install(TARGETS ${PROJECT_NAME}_node
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark other files for installation (e.g. launch and bag files, etc.)
install(
  DIRECTORY launch
  #   # myfile1
  #   # myfile2
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
