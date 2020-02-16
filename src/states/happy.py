import smach
import rospy

from std_msgs.msg import String,Bool,Int32

# define state Idle
class Idle(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['ok'])
        ## Subscriber to the topic /speech_to_text a message of type String that cointains the vocal command converted in text
        self.pub_rgb_light = rospy.Publisher('/rgb_msg', String, queue_size=1)

    def execute(self, userdata):
        rospy.loginfo('Executing state HAPPY')
	
        self.pub_rgb_light.publish("GREEN LIGHT ON")

        return "ok"

