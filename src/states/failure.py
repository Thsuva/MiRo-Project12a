import smach

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image,CompressedImage,Range,Imu
from geometry_msgs.msg import Twist,Pose
import random

import miro_msgs
from miro_msgs.msg import platform_config,platform_sensors,platform_state,platform_mics,platform_control,core_state,core_control,core_config,bridge_config,bridge_stream

import math
import numpy
import time
import sys
from miro_constants import miro

from datetime import datetime
import time

## \file failure.py 
##\brief The class Failure handles the failure state.
## @n FAILURE has:
## @n - output (reset): miro has expressed a sad behavior after a failure and gets back to idle state
class Failure(smach.State):
    ## Constructor
    def __init__(self):
        ## State initialization 
        smach.State.__init__(self, outcomes=['reset'])

        ## Node rate
        self.rate = rospy.get_param('rate',200)
        ## Max number of second allowed
        self.MAX_DURATION = 15

        ## Publisher to the topic /miro/rob01/platform/control a message of type platform_control which corresponds to the "Sad" feedback.
        self.pub_platform_control = rospy.Publisher('/miro/rob01/platform/control',platform_control,queue_size=0)
    
    ## Execute the state: miro show disappointment and sadness 
    def execute(self, userdata):

        r = rospy.Rate(self.rate)

        ## Object of type platform control to publish 
        q = platform_control()

        start_time = time.time()  # Timer initialization
        while not rospy.is_shutdown() and (time.time() - start_time < self.MAX_DURATION):
            # Building behavioral message

            q.eyelid_closure = 0.3
            # [tilt, lift, yaw, pitch] in radiant (tilt and yaw values must be set to 0 due to hardware problem)
            q.body_config = [0.0,1.0,0.0,0.1]
            # [tilt, lift, yaw, pitch] speed in radiant/seconds to reach position, 
            # -1 means "as fast as possible" (tilt and yaw values must be set to 0 due to hardware problem)
            q.body_config_speed = [0.0,-1.0,0.0,-1.0]
            q.lights_raw = [0,0,255,0,0,255,0,0,255,0,0,255,0,0,255,0,0,255]
            q.tail = -1.0
            q.ear_rotate = [1.0,1.0]
            q.body_vel.linear.x = 0.0
            q.body_vel.angular.z = 0.0

            # Pubblish behavioural message 
            self.pub_platform_control.publish(q)
            r.sleep()    

        # Resetting miro position before returning to Idle state
        q = platform_control()
        q.eyelid_closure = 0.0
        # [tilt, lift, yaw, pitch] in radiant (tilt and yaw values must be set to 0 due to hardware problem)
        q.body_config = [0.0,0.45,0.0,-0.2]
        # [tilt, lift, yaw, pitch] speed in radiant/seconds to reach position, 
        # -1 means "as fast as possible" (tilt and yaw values must be set to 0 due to hardware problem)
        q.body_config_speed = [0.0,-1.0,0.0,-1.0]
        self.pub_platform_control.publish(q)

        return 'reset'
