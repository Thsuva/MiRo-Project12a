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

## Function used for conversion from byteArray to String (The values that we get for the head touch sensors are byteArrays)
def fmt(x, f): 
    s = ""
    x = bytearray(x)
    for i in range(0, len(x)):
        if not i == 0:
            s = s + ", "
        s = s + f.format(x[i])
    return s

## \file happy.py
## \brief Class Happy handles the happy state.
## @n HAPPY has:
## @n - outcome (ok): MiRo signals that the goal has been reached
class Happy(smach.State):
    
    ## Constructor
    def __init__(self):
        ## Initialize the state
        smach.State.__init__(self, outcomes=['ok'])

	## Node rate
        self.rate = rospy.get_param('rate',200)

        ## Initialization of head capacitive sensors
        # self.sensors_head = [0, 0, 0, 0]	
        self.h1 = 0
        self.h2 = 0
        self.h3 = 0
        self.h4 = 0
        ## Initialization of bodycapacitive sensors
        # self.sensors_body = [0, 0, 0, 0]
        self.b1 = 0
        self.b2 = 0
        self.b3 = 0
        self.b4 = 0

        ## Subscriber to the topic /miro/rob01/platform/sensors a message of type platform_sensors that cointains the information about the capacitive sensors.
        self.sub_sensors_touch = rospy.Subscriber('/miro/rob01/platform/sensors', platform_sensors, self.callback_touch,queue_size=1)
        ## Publisher to the topic /miro_good a message of type platform_control which corresponds to the "Good" action.
        self.pub_platform_control = rospy.Publisher('/miro/rob01/platform/control',platform_control,queue_size=0)
   
    ## Callback function that saves in class' attributes the capacitive sensor readings converted    
    def callback_touch(self, datasensor):
        '''
        for i in range (0,4):
            self.sensors_head[i] = int(fmt(datasensor.touch_head, '{0:.0f}')[i*3])
            self.sensors_body[i] = int(fmt(datasensor.touch_body, '{0:.0f}')[i*3])
        '''
        
        self.h1 = int(fmt(datasensor.touch_head, '{0:.0f}')[0]) 
        self.h2 = int(fmt(datasensor.touch_head, '{0:.0f}')[3]) 
        self.h3 = int(fmt(datasensor.touch_head, '{0:.0f}')[6])
        self.h4 = int(fmt(datasensor.touch_head, '{0:.0f}')[9])
        self.b1 = int(fmt(datasensor.touch_body, '{0:.0f}')[0])
        self.b2 = int(fmt(datasensor.touch_body, '{0:.0f}')[3]) 
        self.b3 = int(fmt(datasensor.touch_body, '{0:.0f}')[6]) 
        self.b4 = int(fmt(datasensor.touch_body, '{0:.0f}')[9])


    ## Execute the state: MiRo has to show his happiness
    def execute(self, userdata):
        rospy.loginfo('Executing state HAPPY')

        r = rospy.Rate(self.rate)
        q = platform_control()
        count = 0
        start_time = time.time()  # Initialize the timer
        while not rospy.is_shutdown() and (time.time() - start_time < 60):
            
            q.sound_index_P1 = 1

            if self.h1 == 1 or self.h2 == 1 or self.h3 == 1 or self.h4 == 1:  # any(self.sensors_head)
                q.eyelid_closure = 0.4
                q.lights_raw = [255,64,64,255,64,64,255,64,64,255,64,64,255,64,64,255,64,64]
                q.tail = 0.0
                q.body_config = [0.2,0.5,0.2,-0.5]
                q.body_config_speed = [0.0,-1.0,-1.0,-1.0]
                rospy.loginfo('HEAD SENSORS TOUCH')

            elif self.b1 == 1 or self.b2 == 1 or self.b3 == 1 or self.b4 == 1:  # any(self.sensors_body)
                q.eyelid_closure = 0.1
                q.lights_raw = [255,129,0,255,129,0,255,129,0,255,129,0,255,129,0,255,129,0]
                q.tail = 0.0
                q.body_config = [0.0,0.29,-0.6,-0.26]
                q.body_config_speed = [0.0,-1.0,-1.0,-1.0]
                q.ear_rotate = [0.5,0.5]
                rospy.loginfo('BODY SENSORS TOUCH')
            else:
                q.eyelid_closure = 0.0
                q.body_config = [0.0,0.25,0.0,-0.25]
                q.body_config_speed = [0.0,-1.0,-1.0,-1.0]
                q.tail = 68
                q.lights_raw = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                q.ear_rotate = [0.0,0.0]
                rospy.loginfo('NO SENSORS TOUCH')
            
            self.pub_platform_control.publish(q)

            r.sleep()

        return "ok"

