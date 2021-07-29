# UNQ_C1 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: line_to_tensor
def line_to_tensor(line, EOS_int=1):
    """Turns a line of text into a tensor

    Args:
        line (str): A single line of text.
        EOS_int (int, optional): End-of-sentence integer. Defaults to 1.

    Returns:
        list: a list of integers (unicode values) for the characters in the `line`.
    """
    
    # Initialize the tensor as an empty list
    tensor = []
    ### START CODE HERE (Replace instances of 'None' with your code) ###
    # for each character:
    for c in line:
        
        # convert to unicode int
        c_int = ord(c)
        
        # append the unicode integer to the tensor list
        tensor.append(c_int)
    
    # include the end-of-sentence integer
    tensor.append(EOS_int)
    ### END CODE HERE ###

    return tensor