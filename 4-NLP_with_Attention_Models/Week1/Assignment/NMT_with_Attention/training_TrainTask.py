# UNQ_C5
# GRADED 
train_task = training.TrainTask(
    
    ### START CODE HERE (REPLACE INSTANCES OF `None` WITH YOUR CODE) ###
    
    # use the train batch stream as labeled data
    labeled_data= train_batch_stream,
    
    # use the cross entropy loss
    loss_layer= tl.CrossEntropyLoss(),
    
    # use the Adam optimizer with learning rate of 0.01
    optimizer= trax.optimizers.Adam(learning_rate=0.01),
    
    # use the `trax.lr.warmup_and_rsqrt_decay` as the learning rate schedule
    # have 1000 warmup steps with a max value of 0.01
    lr_schedule= trax.lr.warmup_and_rsqrt_decay(1000, 0.01),
    
    # have a checkpoint every 10 steps
    n_steps_per_checkpoint= 10,
    
    ### END CODE HERE ###
)