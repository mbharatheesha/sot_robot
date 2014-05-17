print("sot_youbot")
print("Prologue loaded.")

from dynamic_graph import plug
from dynamic_graph.sot.pr2.robot import Pr2
from dynamic_graph.sot.core import  SOT,FeaturePosition, Task

#from dynamic_graph.sot.youbot.youbot_device import YoubotDevice
from dynamic_graph.entity import PyEntityFactoryClass

Device = PyEntityFactoryClass('YoubotDevice')
robot = Pr2(name = 'Pr2', device = Device('Pr2_device'))
dimension = robot.dynamic.getDimension()
plug(robot.device.state, robot.dynamic.position)

#solver#
solver = SOT ('solver')
solver.setSize (robot.dynamic.getDimension())
plug (solver.control, robot.device.control)

__all__ = ["robot"]

