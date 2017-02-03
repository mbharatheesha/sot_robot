#!/usr/bin/python
import roslib; roslib.load_manifest('dynamic_graph_bridge')
import rospy
import dynamic_graph_bridge_msgs.srv
import sys
import code
import readline
# ATF imports
import unittest
import rospy
import rostest
import tf
import math
import sys
from atf_core import ATF

class RosShell():
    def __init__(self):
        self.cache = ""
        rospy.loginfo('waiting for service...')
        rospy.wait_for_service('run_command')
        self.client = rospy.ServiceProxy(
            'run_command', dynamic_graph_bridge_msgs.srv.RunCommand, True)

    def runcode(self, code, retry = True):
        try:
            if not self.client:
                print("Connection to remote server lost. Reconnecting...")
                self.client = rospy.ServiceProxy(
                    'run_command', dynamic_graph_bridge_msgs.srv.RunCommand, True)
                if retry:
                    print("Retrying previous command...")
                    return self.runcode(code, False)
            response = self.client(code)
            if response.standardoutput != "":
                print response.standardoutput[:-1]
            if response.standarderror != "":
                print response.standarderror[:-1]
            elif response.result != "None":
                #print response.result
                return response.result
        except rospy.ServiceException, e:
            print("Connection to remote server lost. Reconnecting...")
            self.client = rospy.ServiceProxy(
                'run_command', dynamic_graph_bridge_msgs.srv.RunCommand, True)
            if retry:
                print("Retrying previous command...")
                self.runcode(code, False)


# ATF test components

class Application:
    def __init__(self):
        # ATF code
        self.atf = ATF()

        self.sh = RosShell()
        # native app code
        self.pub_freq = 20.0 # Hz
        self.br = tf.TransformBroadcaster()
        rospy.sleep(1) #wait for tf broadcaster to get active (rospy bug?)

    def execute(self):

        # small testblock (circle r=0.5, time=3)
        self.atf.start("testblock_small")
        #Example code#
        # push python commands using clients
        self.sh.runcode('sot.robot.dynamic.position.value')

        self.atf.stop("testblock_small")

#        # large testblock (circle r=1, time=5
#        self.atf.start("testblock_large")
#        self.pub_tf_circle("link1", "link2", radius=2, time=5)
#        self.atf.stop("testblock_large")
#        
#        self.atf.shutdown()
#
#    def pub_tf_circle(self, parent_frame_id, child1_frame_id, radius=1, time=1):
#        rate = rospy.Rate(int(self.pub_freq))
#        for i in range(int(self.pub_freq * time) + 1):
#            t = i / self.pub_freq / time
#            self.br.sendTransform(
#                    (-radius * math.cos(2 * math.pi * t) + radius, -radius * math.sin(2 * math.pi * t), 0),
#                    tf.transformations.quaternion_from_euler(0, 0, 0),
#                    rospy.Time.now(),
#                    child1_frame_id,
#                    parent_frame_id)
#            rate.sleep()

class Test(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def tearDown(self):
        pass

    def test_Recording(self):
        self.app.execute()

if __name__ == '__main__':
    rospy.init_node('test_name')
    if "standalone" in sys.argv:
        app = Application()
        app.execute()
    else:
        rostest.rosrun('application', 'recording', Test, sysargs=None)


