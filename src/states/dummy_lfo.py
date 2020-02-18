import smach
import rospy
import time

from std_msgs.msg import String,Bool,Int32

## \file dummy_lfo.py 
## \brief Class DummyLFO handles the look for object state.
## @n LOOK FOR OBJECT has:
## @n - input (dummy_lfo_in): a vocal command by an user
## @n - outcome (found): the object has been correctly found
## @n - outcome (recognizing_failure): the object has NOT been correctly found
class DummyLFO(smach.State):

    ## Constructor
    def __init__(self):
        ## Initialize the state
        smach.State.__init__(self, outcomes=['found', 'recognizing_failure'],
                                   input_keys=['dummy_lfo_in'])
	self.target = ''
	self.action = ''
	self.color  = ''

    ## Execute the state: MiRo starts looking for a specific object with given shape and colour 
    def execute(self, userdata):
        rospy.loginfo('Executing state DUMMY_LFO')
        
        # This part has to be filled with the actual code (dummy file)
        self.action = userdata.dummy_lfo_in[0]
	self.color  = userdata.dummy_lfo_in[1]
        self.target = userdata.dummy_lfo_in[2]
        
        rospy.loginfo(self.action)
        rospy.loginfo(self.color)
        rospy.loginfo(self.target)
	'''while not rospy.is_shutdown():
            #ACTIVATION COMMAND'''
        if 2 == 2:
            return 'recognizing_failure'

        return 'found'
