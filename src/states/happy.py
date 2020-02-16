import smach
import rospy

from std_msgs.msg import String,Bool,Int32

# define state Happy
class Happy(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['ok'])

        self.pub_rgb_light = rospy.Publisher('/rgb_msg', String, queue_size=1)

    def execute(self, userdata):
        rospy.loginfo('Executing state HAPPY')
	
        self.pub_rgb_light.publish("GREEN_LIGHT_ON")

        return "ok"

