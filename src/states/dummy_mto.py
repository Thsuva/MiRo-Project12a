import smach
import rospy
import time

from std_msgs.msg import String,Bool,Int32
from speech_interaction.msg import Speech2text

# define state Active
class DummyMTO(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['arrived'])

    def execute(self, userdata):
        rospy.loginfo('Executing state DUMMY_MTO')
        
	'''
	while not rospy.is_shutdown():
            #ACTIVATION COMMAND
	'''

        return 'arrived'
