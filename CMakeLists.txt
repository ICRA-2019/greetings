cmake_minimum_required(VERSION 2.8.3)
project(greetings)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION} )

catkin_install_python(PROGRAMS scripts/${PROJECT_NAME}.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
