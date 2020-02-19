import smach
import rospy
import time

from std_msgs.msg import String,Bool,Int32

## \file dummy_mto.py 
## \brief Class DummyMTO handles the move towards object state.
## @n MOVE TOWARDS OBJECT has:
## @n - outcome (arrived): MiRo has arrived to the goal object
class DummyMTO(smach.State):

    ## Constructor
    def __init__(self):
        ## Initialize the state
        smach.State.__init__(self, outcomes=['arrived', 'not_arrived'])

    ## Execute the state: MiRo has to get to a specific object with given shape and colour
    def execute(self, userdata):
        rospy.loginfo('Executing state DUMMY_MTO')
        
        # This part has to be filled with the actual code to move MIRO forward (dummy file)
	'''
	while not rospy.is_shutdown():
            #ACTIVATION COMMAND
	'''
        # This control must check if MIRO has come to destination 
        if 1 == 1:
            return 'arrived'
        # If miro is not arrived yet it will be put in lfo state again and it will correct its trajectory
        return 'not_arived'
