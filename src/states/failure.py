import smach
import rospy
import time

from std_msgs.msg import String,Bool,Int32
from speech_interaction.msg import Speech2text

# define state Active
class Failure(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['reset'])

		self.pub_rgb_light = rospy.Publisher('rgb_msg', String, queue_size=1)
        rospy.init_node('talker', anonymous=True)
        
    def execute(self, userdata):
        self.pub_rgb_light.publish('RED_LIGHT_ON')
        

        return 'reset'
