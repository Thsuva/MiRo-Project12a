def check_presence(list1, list2):
    for key_word in list1:
	if key_word in list2:
            return key_word

    return ''

def do_parsing(text, calling_state):
    return_item = None
    text_lower = str(text).lower()
    text_list = text_lower.split()

    if calling_state == 'ACTIVE':
        VALID_ACTION_LIST = ['go','move']
	VALID_COLOR_LIST  = ['yellow','blue','green']
	VALID_TARGET_LIST = ['ball','circle']

	action = check_presence(text_list, VALID_ACTION_LIST)
	color  = check_presence(text_list, VALID_COLOR_LIST)
	target = check_presence(text_list, VALID_TARGET_LIST)

	if action != '' and color != '' and target != '':
            return_item = (action, color, target)
    
    elif calling_state == 'IDLE':
        WAKE_UP_WORD = 'hello'
	if WAKE_UP_WORD in text_list:
            return_item = WAKE_UP_WORD

    return return_item

