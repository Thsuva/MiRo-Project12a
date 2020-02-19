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

        # Collecting data form the Active state
 
        ## Action to complete
        self.action = userdata.dummy_lfo_in[0]
        ## Color of the target
	self.target_color  = userdata.dummy_lfo_in[1]
        ## Shape of the target
        self.target_shape = userdata.dummy_lfo_in[2]
        # This part has to be filled with the actual code to move MIRO thowards the target (dummy file)
        
        rospy.loginfo(self.action)
        rospy.loginfo(self.target_color)
        rospy.loginfo(self.target_shape)
	'''while not rospy.is_shutdown():
            #ACTIVATION COMMAND'''
        # TODO: this control needs to be bounded to a timer,  after the timer wears off MIRO will give up its research and
        # will go to failure state where it will reset. Since "lfo" and "mto" states are in a loop 
        # remember to initialize the timer at the start of the execute method so that miro will have a set amount of seconds
        # to research the object each time. EXAMPLE OF TIMER USAGE CAN BE FOUND INSIDE THE ACTIVE STATE
        if 1 == 2:
            return 'recognizing_failure'

        return 'found'
