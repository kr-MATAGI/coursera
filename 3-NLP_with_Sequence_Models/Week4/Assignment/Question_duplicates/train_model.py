lr_schedule = trax.lr.warmup_and_rsqrt_decay(400, 0.01)

# UNQ_C4 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: train_model
def train_model(Siamese, TripletLoss, lr_schedule, train_generator=train_generator, val_generator=val_generator, output_dir='model/'):
    """Training the Siamese Model

    Args:
        Siamese (function): Function that returns the Siamese model.
        TripletLoss (function): Function that defines the TripletLoss loss function.
        lr_schedule (function): Trax multifactor schedule function.
        train_generator (generator, optional): Training generator. Defaults to train_generator.
        val_generator (generator, optional): Validation generator. Defaults to val_generator.
        output_dir (str, optional): Path to save model to. Defaults to 'model/'.

    Returns:
        trax.supervised.training.Loop: Training loop for the model.
    """
    output_dir = os.path.expanduser(output_dir)

    ### START CODE HERE (Replace instances of 'None' with your code) ###

    train_task = training.TrainTask(
        labeled_data=train_generator,       # Use generator (train)
        loss_layer=TripletLoss(),         # Use triplet loss. Don't forget to instantiate this object
        optimizer=trax.optimizers.Adam(0.01),          # Don't forget to add the learning rate parameter
        lr_schedule=lr_schedule, # Use Trax multifactor schedule function
    )

    eval_task = training.EvalTask(
        labeled_data=val_generator,       # Use generator (val)
        metrics=[TripletLoss()],          # Use triplet loss. Don't forget to instantiate this object
    )
    
    ### END CODE HERE ###

    training_loop = training.Loop(Siamese(),
                                  train_task,
                                  eval_task=eval_task,
                                  output_dir=output_dir)

    return training_loop