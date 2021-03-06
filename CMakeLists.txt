CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

SET(CXX_DISABLE_WERROR TRUE)
INCLUDE(cmake/base.cmake)
INCLUDE(cmake/cpack.cmake)

set(ROS_BUILD_TYPE RelWithDebInfo)

project(sot_robot)

find_package(catkin REQUIRED COMPONENTS pr2_controller_interface pr2_controller_manager realtime_tools roscpp rospy urdf std_msgs message_generation std_srvs geometry_msgs sensor_msgs tf rospy rqt_gui_py)

find_package(Boost REQUIRED COMPONENTS program_options)


##gui
#find_package(Qt4 COMPONENTS QtCore QtGui REQUIRED)
#include(${QT_USE_FILE})
#include(${QT_USE_FILE})
#add_definitions(-DQT_NO_KEYWORDS)
#qt4_wrap_cpp(MOC_FILES
#  include/gui/myviz.h
#)
#catkin_python_setup()
catkin_package(CATKIN_DEPENDS message_runtime)

SET(PROJECT_NAME sot_robot)
SET(PROJECT_DESCRIPTION "sot controller for ros based robot")
SET(PROJECT_URL "")

#SETUP_PROJECT()

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
set(CMAKE_INSTALL_RPATH "${LIBRARY_OUTPUT_PATH}")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${LIBRARY_OUTPUT_PATH}")
set(PKG_CONFIG_ADDITIONAL_VARIABLES
  ${PKG_CONFIG_ADDITIONAL_VARIABLES}
  plugindirname
  plugindir
  )

# Search for dependencies.
ADD_REQUIRED_DEPENDENCY("jrl-mathtools")
ADD_REQUIRED_DEPENDENCY("jrl-mal")
ADD_REQUIRED_DEPENDENCY("dynamic-graph")
ADD_REQUIRED_DEPENDENCY("dynamic_graph_bridge")
ADD_REQUIRED_DEPENDENCY("dynamic-graph-python")
ADD_REQUIRED_DEPENDENCY("sot-core")
ADD_REQUIRED_DEPENDENCY("sot-dynamic")

# Python
INCLUDE(cmake/python.cmake)
FINDPYTHON()
INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_DIRS} include)
LINK_DIRECTORIES(${PYTHON_LIBRARY_DIRS})

set(SOURCES
    src/sot_robot_controller_threaded_generic.cpp
    src/sot_robot_device.cpp)

set(HEADERS
    include/sot_robot/sot_robot_controller_threaded_generic.h
    include/sot_robot/sot_robot_device.h)



#add_library(sot_robot ${SOURCES_GUI})

add_library(sot_robot SHARED ${HEADERS} ${SOURCES})

target_link_libraries(sot_robot dynamic-graph)
target_link_libraries(sot_robot sot-core)
target_link_libraries(sot_robot dynamic-graph-python)
target_link_libraries(sot_robot ros_bridge)
target_link_libraries(sot_robot ros_interpreter)


#message(cmakeinstall ${CMAKE_INSTALL_LIBDIR})
PKG_CONFIG_USE_DEPENDENCY(sot_robot "dynamic-graph")
PKG_CONFIG_USE_DEPENDENCY(sot_robot "sot-core")
PKG_CONFIG_USE_DEPENDENCY(sot_robot "dynamic-graph-python")

set_target_properties(sot_robot PROPERTIES BUILD_WITH_INSTALL_RPATH True
                      LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)


message(path ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(TARGETS ${PROJECT_NAME}
   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


## copy launch files
install(DIRECTORY launch
   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
   FILES_MATCHING PATTERN "*.launch"
)

install(DIRECTORY robot
   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
## Mark other files for installation (e.g. launch and bag files, etc.)
install(FILES
  robot/pr2_sot_controller.yaml
#   # myfile2
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config
)

install(FILES
  controller_plugins.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

############# GUI ################################
install(FILES gui_plugin.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
install(DIRECTORY resource
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
install(PROGRAMS
  script/rqt_rpc
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
install(PROGRAMS
  script/rqt_rpc_robot
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
message(path ${CMAKE_PREFIX_PATH})

ADD_SUBDIRECTORY(src)
