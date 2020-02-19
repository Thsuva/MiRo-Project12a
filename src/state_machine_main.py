#!/usr/bin/env python

from std_msgs.msg import String,Bool,Int32
from sensor_msgs.msg import Image,CompressedImage,Range,Imu
from geometry_msgs.msg import Twist,Pose
from speech_interaction.msg import Speech2text
from miro_constants import miro
from datetime import datetime

from states.idle import Idle
from states.active import Active
from states.dummy_lfo import DummyLFO
from states.dummy_mto import DummyMTO
from states.failure import Failure
from states.happy import Happy

from miro_msgs.msg import platform_config,platform_sensors,platform_state,platform_mics,platform_control,core_state,core_control,core_config,bridge_config,bridge_stream

# import opencv_apps
# from opencv_apps.msg import CircleArrayStamped

import rospy
import math
import numpy
import time
import sys
import smach
import miro_msgs


## \file state_machine_main.py 
## \brief The node state_machine deals with the building of the state machine's structure.
## @n The architecture of the state machine corresponds to the uml shown in docs/StateMachine.jpg file. 

## \brief Function main initializes the node and builds the state machine
def main():
    ## initialize node sm
    rospy.init_node('state_machine')
    
    ## Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['outcome_end'])

    ## Open the container 'sm' and states to the container
    with sm:
        ## Add Idle state: MiRo is waiting for the activation command
        smach.StateMachine.add('IDLE', Idle(), 
                               transitions={'miro':'ACTIVE'})
        ## Add Active state: MiRo is waiting for moving command
        smach.StateMachine.add('ACTIVE', Active(), 
                               transitions={'successful':'DUMMY_PA',
                                            'time_failure':'FAILURE'},
                               remapping={'active_out':'command'})

        ## Create the sub SMACH state machine 'sm_perform_action'
        sm_perform_action = smach.StateMachine(outcomes=['outcome_end_pa','outcome_end_failure_pa'],
                                               input_keys=['dummy_pa_in'])

        ## Open the container 'sm_perform_action'
        with sm_perform_action:

            ## Add Look for object state: MiRo searches the target object
            smach.StateMachine.add('DUMMY_LFO', DummyLFO(), 
                                   transitions={'found':'DUMMY_MTO', 
                                                'recognizing_failure':'outcome_end_failure_pa'},
                                   remapping={'dummy_lfo_in':'dummy_pa_in'})
            ## Add Move towards object state: MiRo moves towards the target object
            smach.StateMachine.add('DUMMY_MTO', DummyMTO(), 
                                   transitions={'arrived':'outcome_end_pa',
                                                'not_arrived':'DUMMY_LFO'})

        ## Add the 'sm_perform_action' sub SMACH state machine to the main state machine 'sm'
        smach.StateMachine.add('DUMMY_PA', sm_perform_action, 
                               transitions={'outcome_end_pa':'HAPPY',
                                            'outcome_end_failure_pa':'FAILURE'},
                               remapping={'dummy_pa_in':'command'})
        ## Add Failure state: MiRo signals error and goes back to Idle
        smach.StateMachine.add('FAILURE', Failure(), 
                               transitions={'reset':'IDLE'})
        ## Add Happy state: MiRo achieves the goals and signals that he's happy
        smach.StateMachine.add('HAPPY', Happy(), 
                               transitions={'ok':'outcome_end'})

    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()
