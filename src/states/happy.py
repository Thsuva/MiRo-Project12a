import smach
import rospy

from std_msgs.msg import String,Bool,Int32

## \file happy.py 
## \brief Class Happy handles the happy state.
## @n HAPPY has:
## @n - output (ok): MiRo signals that the goal has been reached
class Happy(smach.State):
    
    ## Constructor
    def __init__(self):
        ## Initialize the state
        smach.State.__init__(self, outcomes=['ok'])

        ## Publisher to the topic /rgb_msg, a message of type String which signals to turn lights on and their colour
        self.pub_rgb_light = rospy.Publisher('/rgb_msg', String, queue_size=1)

    ## Execute the state: MiRo has to show his happiness
    def execute(self, userdata):
        rospy.loginfo('Executing state HAPPY')
	
        ## Turn green lights on
        self.pub_rgb_light.publish("GREEN_LIGHT_ON")

        # TODO: This part could be modified in order to show a more complex behaviour

        return "ok"

