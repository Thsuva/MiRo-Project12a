import smach
import rospy

from std_msgs.msg import String,Bool,Int32
from speech_interaction.msg import Speech2text

from parser.parser import do_parsing

# define state Idle
class Idle(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['miro'])
        self.command = String()
        self.min_confidence = .75

        ## Subscriber to the topic /speech_to_text a message of type String that cointains the vocal command converted in text
        self.sub_speech_to_text = rospy.Subscriber('/speech_to_text', Speech2text, self.callback_receive_command,queue_size=1)

    def callback_receive_command(self, text):
        if text.confidence > self.min_confidence:
            self.command = text.transcript

    def execute(self, userdata):
        rospy.loginfo('Executing state IDLE')
	while not rospy.is_shutdown():

            #ACTIVATION COMMAND
            if do_parsing(self.command, 'IDLE') is not None:
                rospy.loginfo('I am awake')
                return 'miro'
