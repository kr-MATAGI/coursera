# UNQ_C4
# GRADED FUNCTION
def ReformerLM(vocab_size=33000, n_layers=2, mode='train', attention_type=tl.SelfAttention):
    """
    Args: 
        vocab_size (int): size of the vocabulary
        n_layers (int): number of decoder layers
        mode (string): setting of the model which can be 'train', 'eval', or 'predict' 
        attention_type(class): attention class to use 
    Returns: 
        model (ReformerLM): a reformer language model implemented in Trax
    """    
    
    ### START CODE HERE (REPLACE INSTANCES OF 'None' WITH YOUR CODE) ###
    # initialize an instance of Trax's ReformerLM class
    model = trax.models.reformer.ReformerLM( 
        # set vocab size
        vocab_size=vocab_size,
        # set number of layers
        n_layers=n_layers,
        # set mode
        mode=mode,
        # set attention type
        attention_type=attention_type
    )
    
    ### END CODE HERE ###
    return model