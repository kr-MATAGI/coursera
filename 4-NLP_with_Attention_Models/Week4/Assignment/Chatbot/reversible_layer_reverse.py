# UNQ_C3
# GRADED FUNCTION: reversible_layer_reverse
def reversible_layer_reverse(y, f, g):
    """
    Args: 
        y (np.array): an input vector or matrix
        f (function): a function which operates on a vector/matrix of the form of 'y'
        g (function): a function which operates on a vector/matrix of the form of 'y'
    Returns: 
        y (np.array): an output vector or matrix whose form is determined by 'y', f and g
    """
    
    # split the input vector into two (* along the last axis because it is the depth dimension)
    y1, y2 = np.split(y, 2, axis=-1)
    
    ### START CODE HERE (REPLACE INSTANCES OF 'None' WITH YOUR CODE) ###
    
    # compute x2 using equation 5
    x2 = y2 - g(y1)
    
    # compute x1 using equation 6
    x1 = y1 - f(x2)
    
    # concatenate x1 and x2 along the depth dimension
    x = np.concatenate([x1, x2], axis=-1)
    
    ### END CODE HERE ### 
    return x