# UNQ_C6
# GRADED FUNCTION
def ReformerLM_output_gen(ReformerLM, start_sentence, vocab_file, vocab_dir, temperature):
    """
    Args:
        ReformerLM:  the Reformer language model you just trained
        start_sentence (string): starting sentence of the conversation
        vocab_file (string): vocabulary filename
        vocab_dir (string): directory of the vocabulary file
        temperature (float): parameter for sampling ranging from 0.0 to 1.0.
            0.0: same as argmax, always pick the most probable token
            1.0: sampling from the distribution (can sometimes say random things)

    Returns:
        generator: yields the next symbol generated by the model
    """
    
    ### START CODE HERE (REPLACE INSTANCES OF 'None' WITH YOUR CODE) ###
    
    # Create input tokens using the the tokenize function
    input_tokens = tokenize(start_sentence, vocab_file, vocab_dir)
    
    # Add batch dimension to array. Convert from (n,) to (x, n) where 
    # x is the batch size. Default is 1. (hint: you can use np.expand_dims() with axis=0)
    input_tokens_with_batch = np.expand_dims(input_tokens, axis=0)
    
    # call the autoregressive_sample_stream function from trax
    output_gen = trax.supervised.decoding.autoregressive_sample_stream( 
        # model
        ReformerLM,
        # inputs will be the tokens with batch dimension
        inputs=input_tokens_with_batch,
        # temperature
        temperature=temperature
    )
    
    ### END CODE HERE ###
    
    return output_gen