# UNQ_C3 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: GRULM
def GRULM(vocab_size=256, d_model=512, n_layers=2, mode='train'):
    """Returns a GRU language model.

    Args:
        vocab_size (int, optional): Size of the vocabulary. Defaults to 256.
        d_model (int, optional): Depth of embedding (n_units in the GRU cell). Defaults to 512.
        n_layers (int, optional): Number of GRU layers. Defaults to 2.
        mode (str, optional): 'train', 'eval' or 'predict', predict mode is for fast inference. Defaults to "train".

    Returns:
        trax.layers.combinators.Serial: A GRU language model as a layer that maps from a tensor of tokens to activations over a vocab set.
    """
    ### START CODE HERE (Replace instances of 'None' with your code) ###
    model = tl.Serial(
      tl.ShiftRight(), # Stack the ShiftRight layer
      tl.Embedding(vocab_size, d_model), # Stack the embedding layer
      [ tl.GRU(n_units=d_model) for n in range(n_layers) ], # Stack GRU layers of d_model units keeping n_layer parameter in mind (use list comprehension syntax)
      tl.Dense(n_units=vocab_size), # Dense layer
      tl.LogSoftmax() # Log Softmax
    )
    ### END CODE HERE ###
    return model