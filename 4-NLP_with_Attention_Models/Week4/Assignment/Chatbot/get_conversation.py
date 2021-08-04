# UNQ_C1
# GRADED FUNCTION: get_conversation
def get_conversation(file, data_db):
    '''
    Args:
        file (string): filename of the dialogue file saved as json
        data_db (dict): dialogue database
    
    Returns:
        string: A string containing the 'text' fields of  data[file]['log'][x]
    '''
    
    # initialize empty string
    result = ''
    
    # get length of file's log list
    len_msg_log = len(data_db[file]['log'])
    
    # set the delimiter strings
    delimiter_1 = ' Person 1: '
    delimiter_2 = ' Person 2: '
    
    # loop over the file's log list
    for i in range(len_msg_log):
        
    ### START CODE HERE (REPLACE INSTANCES OF 'None' WITH YOUR CODE) ###
    
        # get i'th element of file log list
        cur_log = data_db[file]['log'][i]['text']
        
        # check if i is even
        if 0 == i % 2:                   
            # append the 1st delimiter string
            result += delimiter_1
        else: 
            # append the 2nd delimiter string
            result += delimiter_2
        
        # append the message text from the log
        result += cur_log
    
    ### END CODE HERE ###

    return result