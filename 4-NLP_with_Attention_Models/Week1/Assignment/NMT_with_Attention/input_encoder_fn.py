# UNQ_C1
# GRADED FUNCTION
def input_encoder_fn(input_vocab_size, d_model, n_encoder_layers):
    """ Input encoder runs on the input sentence and creates
    activations that will be the keys and values for attention.
    
    Args:
        input_vocab_size: int: vocab size of the input
        d_model: int:  depth of embedding (n_units in the LSTM cell)
        n_encoder_layers: int: number of LSTM layers in the encoder
    Returns:
        tl.Serial: The input encoder
    """
    
    # create a serial network
    input_encoder = tl.Serial( 
        
        ### START CODE HERE (REPLACE INSTANCES OF `None` WITH YOUR CODE) ###
        # create an embedding layer to convert tokens to vectors
        tl.Embedding(input_vocab_size, d_model),
        
        # feed the embeddings to the LSTM layers. It is a stack of n_encoder_layers LSTM layers
        [tl.LSTM(d_model) for _ in range(n_encoder_layers)]
        ### END CODE HERE ###
    )

    return input_encoder