# UNQ_C8
# GRADED FUNCTION

# for making a frequency table easily
from collections import Counter

def rouge1_similarity(system, reference):
    """Returns the ROUGE-1 score between two token lists

    Args:
        system (list of int): tokenized version of the system translation
        reference (list of int): tokenized version of the reference translation

    Returns:
        float: overlap between the two token lists
    """    
    
    ### START CODE HERE (REPLACE INSTANCES OF `None` WITH YOUR CODE) ###
    
    # make a frequency table of the system tokens (hint: use the Counter class)
    sys_counter = Counter(system)
    
    # make a frequency table of the reference tokens (hint: use the Counter class)
    ref_counter = Counter(reference)
    
    # initialize overlap to 0
    overlap = 0
    
    # run a for loop over the sys_counter object (can be treated as a dictionary)
    for token in sys_counter:
        
        # lookup the value of the token in the sys_counter dictionary (hint: use the get() method)
        token_count_sys = sys_counter.get(token, 0)
        
        # lookup the value of the token in the ref_counter dictionary (hint: use the get() method)
        token_count_ref = ref_counter.get(token, 0)
        
        # update the overlap by getting the smaller number between the two token counts above
        overlap += token_count_sys if token_count_sys < token_count_ref else token_count_ref
    
    # get the precision (i.e. number of overlapping tokens / number of system tokens)
    precision = overlap / sum(sys_counter.values())
    
    # get the recall (i.e. number of overlapping tokens / number of reference tokens)
    recall = overlap / sum(ref_counter.values())
    
    if precision + recall != 0:
        # compute the f1-score
        rouge1_score = 2 * (precision * recall / (precision + recall))
    else:
        rouge1_score = 0 
    ### END CODE HERE ###
    
    return rouge1_score
    