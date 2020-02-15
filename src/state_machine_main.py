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

from miro_msgs.msg import platform_config,platform_sensors,platform_state,platform_mics,platform_control,core_state,core_control,core_config,bridge_config,bridge_stream

#import opencv_apps
#from opencv_apps.msg import CircleArrayStamped

import rospy
import math
import numpy
import time
import sys
import smach
import miro_msgs


## \file state_machine_simple.py 
## \brief The node smach_example_state_machine builds a state machine using the smach library
## @n I am the comment with chiocciola enne
def main():
    rospy.init_node('state_machine')
    
    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['outcome_end'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('IDLE', Idle(), 
                               transitions={'miro':'ACTIVE'})
        smach.StateMachine.add('ACTIVE', Active(), 
                               transitions={'successful':'DUMMY_PA',
                                            'time_failure':'outcome_end',
                                            'parsing_failure':'outcome_end'},
                               remapping={'active_out':'command'})

        # Create the sub SMACH state machine perform action
        sm_perform_action = smach.StateMachine(outcomes=['outcome_end_pa'],
                                               input_keys=['dummy_pa_in'])

        # Open the container
        with sm_perform_action:

            # Look for object
            smach.StateMachine.add('DUMMY_LFO', DummyLFO(), 
                                   transitions={'found':'DUMMY_MTO', 
                                                'recognizing_failure':'outcome_end_pa'},
                                   remapping={'dummy_lfo_in':'dummy_pa_in'})
            # Move towards object
            smach.StateMachine.add('DUMMY_MTO', DummyMTO(), 
                                   transitions={'arrived':'outcome_end_pa'})

        smach.StateMachine.add('DUMMY_PA', sm_perform_action, 
                               transitions={'outcome_end_pa':'outcome_end'},
                               remapping={'dummy_pa_in':'command'})

    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()
