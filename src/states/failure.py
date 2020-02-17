import smach
import rospy
import time

from std_msgs.msg import String,Bool,Int32

## \file failure.py 
##\brief The class Failure handles the failure state.
## @n FAILURE has:
## @n - output (reset): miro has expressed a sad behavior after a failure and gets back to idle state
class Failure(smach.State):
    ## Constructor
    def __init__(self):
        ## state initialization 
        smach.State.__init__(self, outcomes=['reset'])
        ## Publisher to the topic /rgb_msg, the messagen is of type String and signals that the light should be truned on, and which color they should have
	self.pub_rgb_light = rospy.Publisher('/rgb_msg', String, queue_size=1)
    
    ## Execute the state: miro show disappointment and sadness 
    def execute(self, userdata):

        self.pub_rgb_light.publish('RED_LIGHT_ON')  # Dummy action string for debug
        # TODO: Here could be added code to express a more complex behaviour before resetting to idle state
        

        return 'reset'
