# UNQ_C4 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: evaluate_prediction
def evaluate_prediction(pred, labels, pad):
    """
    Inputs:
        pred: prediction array with shape 
            (num examples, max sentence length in batch, num of classes)
        labels: array of size (batch_size, seq_len)
        pad: integer representing pad character
    Outputs:
        accuracy: float
    """
    ### START CODE HERE (Replace instances of 'None' with your code) ###
## step 1 ##
    outputs = np.argmax(pred, axis=2)
    print("outputs shape:", outputs.shape)

## step 2 ##
    mask = np.where(labels == pad, False, True)
    print("mask shape:", mask.shape, "mask[0][20:30]:", mask[0][20:30])
## step 3 ##
    accuracy = np.sum(outputs==labels)/float(np.sum(mask))
    ### END CODE HERE ###
    return accuracy