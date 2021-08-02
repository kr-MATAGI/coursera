# UNQ_C3 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: TripletLossFn
def TripletLossFn(v1, v2, margin=0.25):
    """Custom Loss function.

    Args:
        v1 (numpy.ndarray): Array with dimension (batch_size, model_dimension) associated to Q1.
        v2 (numpy.ndarray): Array with dimension (batch_size, model_dimension) associated to Q2.
        margin (float, optional): Desired margin. Defaults to 0.25.

    Returns:
        jax.interpreters.xla.DeviceArray: Triplet Loss.
    """
    ### START CODE HERE (Replace instances of 'None' with your code) ###
    
    # use fastnp to take the dot product of the two batches (don't forget to transpose the second argument)
    scores = fastnp.dot( v1/fastnp.sqrt(np.sum(v1 * v1, axis=1, keepdims=True)), (v2/fastnp.sqrt(np.sum(v2 * v2, axis=1, keepdims=True))).T ) # pairwise cosine sim
    # calculate new batch size
    batch_size = len(scores)
    # use fastnp to grab all postive `diagonal` entries in `scores`
    positive = fastnp.diagonal(scores)  # the positive ones (duplicates)
    # multiply `fastnp.eye(batch_size)` with 2.0 and subtract it out of `scores`
    negative_without_positive = scores - (fastnp.eye(batch_size) * 2.0)
    
    # take the row by row `max` of `negative_without_positive`. 
    # Hint: negative_without_positive.max(axis = [?])  
    closest_negative = negative_without_positive.max(axis=1)
    
    # subtract `fastnp.eye(batch_size)` out of 1.0 and do element-wise multiplication with `scores`
    negative_zero_on_duplicate = (1.0 - fastnp.eye(batch_size)) * scores
    
    # use `fastnp.sum` on `negative_zero_on_duplicate` for `axis=1` and divide it by `(batch_size - 1)` 
    mean_negative = fastnp.sum(negative_zero_on_duplicate, axis=1)
    # compute `fastnp.maximum` among 0.0 and `A`
    # A = subtract `positive` from `margin` and add `closest_negative` 
    triplet_loss1 = fastnp.maximum(-1*positive + closest_negative + margin, 0)
    # compute `fastnp.maximum` among 0.0 and `B`
    # B = subtract `positive` from `margin` and add `mean_negative`
    triplet_loss2 = fastnp.maximum(-1*positive + mean_negative + margin, 0)
    # add the two losses together and take the `fastnp.mean` of it
    triplet_loss = fastnp.mean(triplet_loss1 + triplet_loss2)
    
    ### END CODE HERE ###
    
    return triplet_loss