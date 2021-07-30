# UNQ_C5 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: test_model
def test_model(preds, target):
    """Function to test the model.

    Args:
        preds (jax.interpreters.xla.DeviceArray): Predictions of a list of batches of tensors corresponding to lines of text.
        target (jax.interpreters.xla.DeviceArray): Actual list of batches of tensors corresponding to lines of text.

    Returns:
        float: log_perplexity of the model.
    """
    ### START CODE HERE (Replace instances of 'None' with your code) ###
    print(preds.shape, target.shape)
    total_log_ppx = np.sum(preds * tl.one_hot(target, preds.shape[-1]), axis= -1) # HINT: tl.one_hot() should replace one of the Nones
    print(total_log_ppx.shape)
    
    non_pad = 1.0 - np.equal(target, 0)          # You should check if the target equals 0
    ppx = total_log_ppx * non_pad                             # Get rid of the padding

    log_ppx = np.sum(ppx) / np.sum(non_pad)
    ### END CODE HERE ###
    
    return -log_ppx