export PATH=$DEVEL_DIR/install/bin:$DEVEL_DIR/install/sbin:$PATH
export PKG_CONFIG_PATH=$DEVEL_DIR/install/lib/pkgconfig:/opt/ros/indigo/lib/pkgconfig/:/usr/lib/pkgconfig/:/usr/local/lib/pkgconfig/
export PYTHONPATH=$DEVEL_DIR/install/lib/python2.7/site-packages:$DEVEL_DIR/install/lib/python2.7/dist-packages:/opt/ros/indigo/lib/python2.7/dist-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$DEVEL_DIR/install/lib:/opt/ros/indigo/lib:usr/local/lib:usr/install/lib:$LD_LIBRARY_PATH

if [ -f $DEVEL_DIR/install/setup.bash ]; then
   source $DEVEL_DIR/install/setup.bash
else
   source /opt/ros/indigo/setup.bash
fi
export ROS_PACKAGE_PATH=$DEVEL_DIR/src:$DEVEL_DIR/install/lib:$ROS_PACKAGE_PATH
