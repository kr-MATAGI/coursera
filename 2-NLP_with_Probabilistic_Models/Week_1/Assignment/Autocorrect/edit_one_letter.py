# UNQ_C8 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# UNIT TEST COMMENT: Candidate for Table Driven Tests
# GRADED FUNCTION: edit_one_letter
def edit_one_letter(word, allow_switches = True):
    """
    Input:
        word: the string/word for which we will generate all possible wordsthat are one edit away.
    Output:
        edit_one_set: a set of words with one possible edit. Please return a set. and not a list.
    """
    
    edit_one_set = set()
    
    ### START CODE HERE ###
    del_func = delete_letter(word)
    sw_func = switch_letter(word)
    re_func = replace_letter(word)
    ins_func = insert_letter(word) 
    
    for item in del_func: edit_one_set.add(item)
    for item in sw_func: edit_one_set.add(item)
    for item in re_func: edit_one_set.add(item)
    for item in ins_func: edit_one_set.add(item)
    

    ### END CODE HERE ###

    return edit_one_set
    
    
    
    
tmp_word = "at"
tmp_edit_one_set = edit_one_letter(tmp_word)
# turn this into a list to sort it, in order to view it
tmp_edit_one_l = sorted(list(tmp_edit_one_set))

print(f"input word {tmp_word} \nedit_one_l \n{tmp_edit_one_l}\n")
print(f"The type of the returned object should be a set {type(tmp_edit_one_set)}")
print(f"Number of outputs from edit_one_letter('at') is {len(edit_one_letter('at'))}")    