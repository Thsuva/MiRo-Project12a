
## \file parser.py 
## \brief The functions inside parser.py are usefull in order to extract information and keywords from the string published in the topic '/speech to text'. It's return depends on various factor and can eather be a triple, a single word,  or a None object.
## @n The string gets changed in lower case than transformed in a list of single word. 
## @n If the calling state is ACTIVE each element of the firts list are compared with each element of standard allowed keyword for each of three category. If a keyword for each category is found in the list a triplet is made with the result and is returned.
## @n If the calling state is IDLE the element in the list are compared to a 'wakeup word' and if that is present its returned. 
## @n The standard return for this funcion is a None object that signifies that an error occurred and not enough information has been extracted from the speech to text string.

## Simple function that check if one of the key_word in list1 is present in list2 and returns it. Otherwise it retrurns an empty string
def check_presence(list1, list2):
    for key_word in list1:
	if key_word in list2:
            return key_word

    return ''

## The function deals with the set up for the searching of key_word  
## @n If the calling state is ACTIVE it repeat the search 3 times looking for keyword inside 3 list of different category returning a list with on item from each list if found or None otherwise.
## @n If the calling state is IDLE it looks for the wake_up_word inside the parsed string returning it if it is found or None otherwise. 
def do_parsing(text, calling_state):

    # declaration and formatting

    return_item = None  # std retrun item  
    text_lower = str(text).lower()  # lower case text
    text_list = text_lower.split()  # list of lower case word

    # active state routine
    if calling_state == 'ACTIVE':
        # declaration of valid items
        VALID_ACTION_LIST = ['go','move']  # keyword for allowed action
	VALID_COLOR_LIST  = ['yellow','blue','green','red']  # keyword for allowed colors
	VALID_TARGET_LIST = ['ball','circle']  # keyword for allowed shapes

        # looking for keyword in text_list
	action = check_presence(text_list, VALID_ACTION_LIST)
	color  = check_presence(text_list, VALID_COLOR_LIST)
	target = check_presence(text_list, VALID_TARGET_LIST)

	if action != '' and color != '' and target != '':
            return_item = (action, color, target)  # return_item is now a triple

    # idle state routine
    elif calling_state == 'IDLE':
        WAKE_UP_WORD = 'hello'  # wake up word for miro (now hello for semplicity)
	if WAKE_UP_WORD in text_list:
            return_item = WAKE_UP_WORD  # return_item is now the wake up word

    return return_item

