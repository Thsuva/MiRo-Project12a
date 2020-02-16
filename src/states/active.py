import smach
import rospy
import time

from std_msgs.msg import String,Bool,Int32
from speech_interaction.msg import Speech2text

from parser.parser import do_parsing

# define state Active
class Active(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['successful', 'time_failure'],
                                   output_keys=['active_out'])
        self.command = String()
        self.min_confidence = .65

        ## Subscriber to the topic /speech_to_text a message of type String that cointains the vocal command converted in text
        self.sub_speech_to_text = rospy.Subscriber('/speech_to_text', Speech2text, self.callback_receive_command,queue_size=1)

    def callback_receive_command(self, text):
        if text.confidence > self.min_confidence:
            self.command = text.transcript

    def execute(self, userdata):
        rospy.loginfo('Executing state ACTIVE')
        start_time = time.time()
	while not rospy.is_shutdown() and (time.time() - start_time < 30):
            #ACTIVATION COMMAND
	    parsed_command = do_parsing(self.command, 'ACTIVE')
            if parsed_command is not None:
                rospy.loginfo(parsed_command)
                userdata.active_out = [parsed_command[0], parsed_command[1], parsed_command[2]]
                return 'successful'

        return 'time_failure'
