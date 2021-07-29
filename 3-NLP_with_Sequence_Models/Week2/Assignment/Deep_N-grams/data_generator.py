# UNQ_C2 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: data_generator
def data_generator(batch_size, max_length, data_lines, line_to_tensor=line_to_tensor, shuffle=True):
    """Generator function that yields batches of data

    Args:
        batch_size (int): number of examples (in this case, sentences) per batch.
        max_length (int): maximum length of the output tensor.
        NOTE: max_length includes the end-of-sentence character that will be added
                to the tensor.  
                Keep in mind that the length of the tensor is always 1 + the length
                of the original line of characters.
        data_lines (list): list of the sentences to group into batches.
        line_to_tensor (function, optional): function that converts line to tensor. Defaults to line_to_tensor.
        shuffle (bool, optional): True if the generator should generate random batches of data. Defaults to True.

    Yields:
        tuple: two copies of the batch (jax.interpreters.xla.DeviceArray) and mask (jax.interpreters.xla.DeviceArray).
        NOTE: jax.interpreters.xla.DeviceArray is trax's version of numpy.ndarray
    """
    # initialize the index that points to the current position in the lines index array
    index = 0
    
    # initialize the list that will contain the current batch
    cur_batch = []
    
    # count the number of lines in data_lines
    num_lines = len(data_lines)
    
    # create an array with the indexes of data_lines that can be shuffled
    lines_index = [*range(num_lines)]
    
    # shuffle line indexes if shuffle is set to True
    if shuffle:
        rnd.shuffle(lines_index)
    
    ### START CODE HERE (Replace instances of 'None' with your code) ###
    while True:
        
        # if the index is greater or equal than to the number of lines in data_lines
        if index >= num_lines:
            # then reset the index to 0
            index = 0
            # shuffle line indexes if shuffle is set to True
            if shuffle:
                rnd.shuffle(lines_index)
            
        # get a line at the `lines_index[index]` position in data_lines
        line = data_lines[lines_index[index]]
        
        # if the length of the line is less than max_length
        if len(line) < max_length:
            # append the line to the current batch
            cur_batch.append(line)
            
        # increment the index by one
        index += 1
        
        # if the current batch is now equal to the desired batch size
        if len(cur_batch) == batch_size:
            
            batch = []
            mask = []
            
            # go through each line (li) in cur_batch
            for li in cur_batch:
                # convert the line (li) to a tensor of integers
                tensor = line_to_tensor(li)
                
                # Create a list of zeros to represent the padding
                # so that the tensor plus padding will have length `max_length`
                pad = [0] * (max_length - len(tensor))
                
                # combine the tensor plus pad
                tensor_pad = tensor + pad
                
                # append the padded tensor to the batch
                batch.append(tensor_pad)

                # A mask for  tensor_pad is 1 wherever tensor_pad is not
                # 0 and 0 wherever tensor_pad is 0, i.e. if tensor_pad is
                # [1, 2, 3, 0, 0, 0] then example_mask should be
                # [1, 1, 1, 0, 0, 0]
                # Hint: Use a list comprehension for this
                example_mask = [1 if 0 != x else 0 for x in tensor_pad  ]
                mask.append(example_mask)
               
            # convert the batch (data type list) to a trax's numpy array
            batch_np_arr = np.array(batch)
            mask_np_arr = np.array(mask)
            
            ### END CODE HERE ##
            
            # Yield two copies of the batch and mask.
            yield batch_np_arr, batch_np_arr, mask_np_arr
            
            # reset the current batch to an empty list
            cur_batch = []