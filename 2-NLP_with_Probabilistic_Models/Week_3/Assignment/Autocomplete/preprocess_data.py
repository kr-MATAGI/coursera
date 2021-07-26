# UNQ_C7 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
### GRADED_FUNCTION: preprocess_data ###
def preprocess_data(train_data, test_data, count_threshold):
    """
    Preprocess data, i.e.,
        - Find tokens that appear at least N times in the training data.
        - Replace tokens that appear less than N times by "<unk>" both for training and test data.        
    Args:
        train_data, test_data: List of lists of strings.
        count_threshold: Words whose count is less than this are 
                      treated as unknown.
    
    Returns:
        Tuple of
        - training data with low frequent words replaced by "<unk>"
        - test data with low frequent words replaced by "<unk>"
        - vocabulary of words that appear n times or more in the training data
    """
    ### START CODE HERE (Replace instances of 'None' with your code) ###

    # Get the closed vocabulary using the train data
    vocabulary = [ x for data in train_data for x in data ]
    # [['sky', 'is', 'blue', '.'], ['leaves', 'are', 'green']] -> ['sky', 'is', 'blue', '.', 'leaves', 'are', 'green']
    
    # For the train data, replace less common words with "<unk>"
    train_data_replaced = replace_oov_words_by_unk(train_data, vocabulary)
    # [ [x if count_threshold <= vocabulary.count(x) else '<unk>' for x in data] for data in train_data]
    
    # [['sky', 'is', 'blue', '.'], ['leaves', 'are', 'green']] -> 
    # [['sky', 'is', 'blue', '.'], ['leaves', 'are', 'green']]
    
    # For the test data, replace less common words with "<unk>"
    test_data_replaced = replace_oov_words_by_unk(test_data, vocabulary)
    # [ [x if count_threshold <= vocabulary.count(x) else '<unk>' for x in data] for data in test_data ]
    # [['roses', 'are', 'red', '.']]  ->
    # [['<unk>', 'are', '<unk>', '.']]
    
    ### END CODE HERE ###
    return train_data_replaced, test_data_replaced, vocabulary
    
    

# test your code
tmp_train = [['sky', 'is', 'blue', '.'],
     ['leaves', 'are', 'green']]
tmp_test = [['roses', 'are', 'red', '.']]

tmp_train_repl, tmp_test_repl, tmp_vocab = preprocess_data(tmp_train, 
                                                           tmp_test, 
                                                           count_threshold = 1)

print("tmp_train_repl")
print(tmp_train_repl)
print()
print("tmp_test_repl")
print(tmp_test_repl)
print()
print("tmp_vocab")
print(tmp_vocab)