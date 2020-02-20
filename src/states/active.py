import smach
import rospy
import time

from std_msgs.msg import String,Bool,Int32
from speech_interaction.msg import Speech2text

from parser.parser import do_parsing

## \file active.py 
##\brief The class Active handles the active state.
## @n ACTIVE has:
## @n - output (active_out): a list containing an action, a color and a target given by the parser and not empty. It's the output for the successful outcome.
## @n - outcome (successful): miro menaged to understand a command given by the user and get ready to execute it.
## @n - outcome (time_failure): miro didnt menaged to understand a command in the time window given, and moves to failure state.

class Active(smach.State):
    ## Constructor
    def __init__(self):
        ## Initialize the state
        smach.State.__init__(self, outcomes=['successful', 'time_failure'],
                                   output_keys=['active_out'])

        ## Stirng object to evaluate
        self.command = String()
        ## Min confidence allowed
        self.MIN_CONFIDENCE = .75
        ## Max number of seconds allowed for this state
        self.MAX_DURATION = 40

        ## Subscriber to the topic /speech_to_text a message of type Speech2text that cointains:
        ## - language found for the string
        ## - the vocal command converted in text
        ## - confidence of the transcription
        self.sub_speech_to_text = rospy.Subscriber('/speech_to_text', Speech2text, self.callback_receive_command,queue_size=1)
        ## Publisher to the topic /rgb_msg, the messagen is of type String and signals that the light should be truned on, and which color they should have
        self.pub_rgb_light = rospy.Publisher('/rgb_msg', String, queue_size=1)

    ## Callback function that receive and save the user's voice command as text if the confidence exceed a set threshold
    def callback_receive_command(self, text):
        if text.confidence > self.MIN_CONFIDENCE:
            self.command = text.transcript
    
    ## Execute the state: MiRo has 30 second to try and fully understand a command
    def execute(self, userdata):
        rospy.loginfo('Executing state ACTIVE')
        self.pub_rgb_light.publish("BLUE_LIGHT_ON") # Dummy action string for debug
        start_time = time.time()  # Initialize the timer
        
        # While loop with 30 sec count down
	while not rospy.is_shutdown() and (time.time() - start_time < self.MAX_DURATION):
            
            # Parsing of the text
	    parsed_command = do_parsing(self.command, 'ACTIVE')

            if parsed_command is not None:
                rospy.loginfo(parsed_command)
                userdata.active_out = [parsed_command[0], parsed_command[1], parsed_command[2]]  # Setting output 
                self.command = String()
                return 'successful'

        return 'time_failure'
