# sot_robot

Author: Nirmal Giftsun

Refactored By: Mukunda Bharatheesha

##Description
sot_robot is a ROS based real time controller which loads 'Stack of Tasks' to perform Hierarchical Task Function based 
Control
##Installation on ubuntu-14.04 with ROS Indigo

To install all the packages on ubuntu 14.04 LTS, you should do the following
steps:

  1. install by apt-get (see http://wiki.ros.org/indigo/Installation/Ubuntu)
    - ros-indigo-desktop-full
    - ros-indigo-libccd
    - ros-indigo-srdfdom
    - ros-indigo-robot-model
    - ros-indigo-ros-control
    - ros-indigo-gazebo-ros-control
    - ros-indigo-realtime-tools
    - ros-indigo-pr2-controller-interface
    - ros-indigo-pr2-controller-manager
    - ros-indigo-control-toolbox
    - ros-indigo-ur-modern-driver
    - git
    - gfortran
    - libblas-dev
    - libblas-doc (optional)
    - liblapacke-dev
    - liblapacke-doc (optional)
    - python-sphinx
    - libbullet-dev
        

  2. Choose a directory on you file system and define the environment
     variable DEVEL_DIR with the full path to this directory.
     - the packages will be cloned into $DEVEL_DIR/src,
     - the packages will be installed in $DEVEL_DIR/install.
     It is recommanded to set variable DEVEL_DIR in your .bashrc for future use.

  3. Copy Config and Makefile from scripts/installation
      -  wget -O $DEVEL_DIR/config.sh https://raw.githubusercontent.com/mbharatheesha/sot_robot/indigo/script/installation/config.sh
      -  wget -O $DEVEL_DIR/src/Makefile https://raw.githubusercontent.com/mbharatheesha/sot_robot/indigo/script/installation/Makefile
  
  4. cd into $DEVEL_DIR and type

    source config.sh

  5. cd into $DEVEL_DIR/src and type

    make all
  
### Testing

      roslaunch sot_robot sot_ur_bringup_sim.launch

      roslaunch sot_robot spawn_ur_controller.launch
  
      rosrun rviz rviz

* Start the python interactor 

      rosrun dynamic_graph_bridge run_command
* Run the following.
      sot.initializeRobot()
      sot.startRobot()
      sot.setRobotPosture((0,0,0,0,0,0,0,0,0,0,0,0))

  The first six elements are x,y,z,r,p,y followed by six joints of the ur5 arm.

* Verify if the joint values manifest in rviz

### Testing in UR SIM

* Start the ur simulator

* Launch the ur robot
        roslaunch sot_ur_bringup_real_sim.launch
* Launch the sot controller
        roslaunch spawn_ur_controller.launch
* Start the python interactor 

      rosrun dynamic_graph_bridge run_command
* Play with the joint positions to check the value

      sot.posture_feature.posture.feature.value = (0,0,0,0,0,0,0,0,0,0,0,0)
