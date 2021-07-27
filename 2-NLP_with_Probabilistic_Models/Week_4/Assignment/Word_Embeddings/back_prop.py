# UNQ_C4 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: back_prop
def back_prop(x, yhat, y, h, W1, W2, b1, b2, batch_size):
    '''
    Inputs: 
        x:  average one hot vector for the context 
        yhat: prediction (estimate of y)
        y:  target vector
        h:  hidden vector (see eq. 1)
        W1, W2, b1, b2:  matrices and biases  
        batch_size: batch size 
     Outputs: 
        grad_W1, grad_W2, grad_b1, grad_b2:  gradients of matrices and biases   
    '''
    ### START CODE HERE (Replace instanes of 'None' with your code) ###
    
    # Compute l1 as W2^T (Yhat - Y)
    # Re-use it whenever you see W2^T (Yhat - Y) used to compute a gradient
    l1 = np.dot(W2.T, yhat-y)
    # Apply relu to l1
    l1 = np.where(l1 < 0, 0, l1)
    # Compute the gradient of W1
    grad_W1 = np.dot(l1, x.T)/batch_size
    # Compute the gradient of W2
    grad_W2 = np.dot(yhat - y, h.T)/batch_size
    # Compute the gradient of b1
    grad_b1 = np.sum(l1/batch_size, axis=1, keepdims=True)
    # Compute the gradient of b2
    grad_b2 = np.sum((yhat - y)/batch_size, axis=1, keepdims=True)
    ### END CODE HERE ###
    
    return grad_W1, grad_W2, grad_b1, grad_b2