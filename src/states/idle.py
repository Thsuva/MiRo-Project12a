import smach
import rospy

from std_msgs.msg import String,Bool,Int32
from speech_interaction.msg import Speech2text

from parser.parser import do_parsing

## \file idle.py 
##\brief The class Idle handles the idle state.
## @n IDLE has:
## @n - outcome (miro): miro has heard its wake up word and gets to Active state
class Idle(smach.State):
    ## Constructor
    def __init__(self):
        ## Initialize the state
        smach.State.__init__(self, outcomes=['miro'])
        self.command = String()  # String to evaluate 
        self.min_confidence = .75  # min confidence allowed

        ## Subscriber to the topic /speech_to_text a message of type Speech2text that cointains:
        ## - language found for the string
        ## - the vocal command converted in text
        ## - confidence of the transcription
        self.sub_speech_to_text = rospy.Subscriber('/speech_to_text', Speech2text, self.callback_receive_command,queue_size=1)

    ## Callback function that receive and save the user's voice command as text if the confidence exceed a set threshold
    def callback_receive_command(self, text):
        if text.confidence > self.min_confidence:
            self.command = text.transcript

    ## Execute the state: miro waits for the wake up call
    def execute(self, userdata):
        rospy.loginfo('Executing state IDLE')
	while not rospy.is_shutdown():
            # Parsing of the text
            if do_parsing(self.command, 'IDLE') is not None:
                # State change
                rospy.loginfo('I am awake')
                self.command = String()
                return 'miro'
