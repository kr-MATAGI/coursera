from trax.supervised import training

# UNQ_C4 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: train_model
def train_model(model, data_generator, batch_size=32, max_length=64, lines=lines, eval_lines=eval_lines, n_steps=1, output_dir='model/'): 
    """Function that trains the model

    Args:
        model (trax.layers.combinators.Serial): GRU model.
        data_generator (function): Data generator function.
        batch_size (int, optional): Number of lines per batch. Defaults to 32.
        max_length (int, optional): Maximum length allowed for a line to be processed. Defaults to 64.
        lines (list, optional): List of lines to use for training. Defaults to lines.
        eval_lines (list, optional): List of lines to use for evaluation. Defaults to eval_lines.
        n_steps (int, optional): Number of steps to train. Defaults to 1.
        output_dir (str, optional): Relative path of directory to save model. Defaults to "model/".

    Returns:
        trax.supervised.training.Loop: Training loop for the model.
    """
    
    ### START CODE HERE (Replace instances of 'None' with your code) ###
    bare_train_generator = data_generator(batch_size, max_length, lines)
    infinite_train_generator = itertools.cycle(bare_train_generator)
    
    bare_eval_generator = data_generator(batch_size, max_length, eval_lines)
    infinite_eval_generator = itertools.cycle(bare_eval_generator)
   
    train_task = training.TrainTask(
        labeled_data=bare_train_generator, # Use infinite train data generator
        loss_layer=tl.CrossEntropyLoss(),   # Don't forget to instantiate this object
        optimizer=trax.optimizers.Adam(learning_rate=0.0005)     # Don't forget to add the learning rate parameter
    )

    eval_task = training.EvalTask(
        labeled_data=infinite_eval_generator,    # Use infinite eval data generator
        metrics=[tl.CrossEntropyLoss(), tl.Accuracy()], # Don't forget to instantiate these objects
        n_eval_batches=3      # For better evaluation accuracy in reasonable time
    )
    
    training_loop = training.Loop(model,
                                  train_task,
                                  eval_task=eval_task,
                                  output_dir=output_dir)

    training_loop.run(n_steps=n_steps)
    
    ### END CODE HERE ###
    
    # We return this because it contains a handle to the model, which has the weights etc.
    return training_loop
