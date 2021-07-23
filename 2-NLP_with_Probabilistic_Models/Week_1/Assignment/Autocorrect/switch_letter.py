nice
[('', 'nice'), ('n', 'ice'), ('ni', 'ce'), ('nic', 'e')] 
[ince, ncie, niec]



eta
[('', 'eta'), ('e', 'ta'), ('et', 'a')]
[tea, eat]

# UNQ_C5 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# UNIT TEST COMMENT: Candidate for Table Driven Tests
# GRADED FUNCTION: switches
def switch_letter(word, verbose=False):
    '''
    Input:
        word: input string
     Output:
        switches: a list of all possible strings with one adjacent charater switched
    ''' 
    
    switch_l = []
    split_l = []
    
    ### START CODE HERE ###
    split_l = [ (word[:idx], word[idx:]) for idx in range(len(word))]
    
    switch_l = [ L[:len(L)-1] + R[:1] + L[len(L)-1] + R[1:] for L,R in split_l if L]
    
    '''
    for L,R in split_l:
        L_len = len(L) - 1
        if L:
            item = L[:L_len] + R[:1] + L[L_len] + R[1:]
            switch_l.append(item)
    '''
    
    ### END CODE HERE ###
    
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}") 

    return switch_l
	
	
switch_word_l = switch_letter(word="eta", verbose=True)