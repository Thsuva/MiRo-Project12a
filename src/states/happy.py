import smach
import rospy

from std_msgs.msg import String,Bool,Int32

## \file happy.py 
## \brief Class Happy handles the happy state.
## @n HAPPY has:
## @n - outcome (ok): MiRo signals that the goal has been reached
class Happy(smach.State):
    
    ## Constructor
    def __init__(self):
        ## Initialize the state
        smach.State.__init__(self, outcomes=['ok'])

        ## Publisher to the topic /rgb_msg, the message is of type String and signals to turn lights on and their colour
        self.pub_rgb_light = rospy.Publisher('/rgb_msg', String, queue_size=1)

    ## Execute the state: MiRo has to show his happiness
    def execute(self, userdata):
        rospy.loginfo('Executing state HAPPY')

        self.pub_rgb_light.publish("GREEN_LIGHT_ON") # Dummy action string for debug

        # TODO: This part could be modified in order to show a more complex behaviour

        return "ok"

