import smach
import rospy
import time

from std_msgs.msg import String,Bool,Int32
from speech_interaction.msg import Speech2text

# define state Active
class DummyLFO(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['found', 'recognizing_failure'],
                                   input_keys=['dummy_lfo_in'])
	self.target = ''
	self.action = ''
	self.color  = ''

    def execute(self, userdata):
        rospy.loginfo('Executing state DUMMY_LFO')
        
        self.action = userdata.dummy_lfo_in[0]
	self.color  = userdata.dummy_lfo_in[1]
        self.target = userdata.dummy_lfo_in[2]
        
        rospy.loginfo(self.action)
        rospy.loginfo(self.color)
        rospy.loginfo(self.target)
	'''while not rospy.is_shutdown():
            #ACTIVATION COMMAND'''
        if 1 == 2:
            return 'recognizing_failure'

        return 'found'
