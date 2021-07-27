# UNQ_C3 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: forward_prop
def forward_prop(x, W1, W2, b1, b2):
    '''
    Inputs: 
        x:  average one hot vector for the context 
        W1, W2, b1, b2:  matrices and biases to be learned
     Outputs: 
        z:  output score vector
    '''
    
    ### START CODE HERE (Replace instances of 'None' with your own code) ###    
    
    # Calculate h
    h = np.dot(W1, x) + b1
    
    # Apply the relu on h (store result in h)
    h = np.where(h < 0, 0, h)
    
    # Calculate z
    z = np.dot(W2, h) + b2
    
    ### END CODE HERE ###

    return z, h