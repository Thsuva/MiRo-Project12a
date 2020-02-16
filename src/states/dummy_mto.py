import smach
import rospy
import time

from std_msgs.msg import String,Bool,Int32

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
