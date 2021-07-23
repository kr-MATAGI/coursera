# UNQ_C10 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# UNIT TEST COMMENT: Candidate for Table Driven Tests
# GRADED FUNCTION: get_corrections
def get_corrections(word, probs, vocab, n=2, verbose = False):
    '''
    Input: 
        word: a user entered string to check for suggestions
        probs: a dictionary that maps each word to its probability in the corpus
        vocab: a set containing all the vocabulary
        n: number of possible word corrections you want returned in the dictionary
    Output: 
        n_best: a list of tuples with the most probable n corrected words and their probabilities.
    '''
    
    suggestions = []
    n_best = []
    
    ### START CODE HERE ###
    vocab_sugg_l = list()
    one_letter_l = list()
    two_letter_l = list()
    else_sugg_l = list()
    
    one_letter_set = edit_one_letter(word)
    two_letter_set = edit_two_letters(word)
    
    # vocab
    if word in vocab: vocab_sugg_l.append(word)
    
    # edit_one
    for item in one_letter_set:
        if item in vocab: one_letter_l.append(item)
        else_sugg_l.append(item)
        
    # edit_two
    for item in two_letter_set:
        if item in vocab: two_letter_l.append(item)
        else_sugg_l.append(item)
    
    suggestions = vocab_sugg_l or one_letter_l or two_letter_l or else_sugg_l
    
    for sugg in suggestions:
        n_best.append((sugg, probs.get(sugg, 0)))
    n_best = sorted(n_best, key=lambda x:x[1])[::-1]
    n_best = n_best[:n]
    
    ### END CODE HERE ###
    
    if verbose: print("entered word = ", word, "\nsuggestions = ", suggestions)

    return n_best
    
# Test your implementation - feel free to try other words in my word
my_word = 'dys'
tmp_corrections = get_corrections(my_word, probs, vocab, 2, verbose=True) # keep verbose=True
for i, word_prob in enumerate(tmp_corrections):
    print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")

# CODE REVIEW COMMENT: using "tmp_corrections" insteads of "cors". "cors" is not defined
print(f"data type of corrections {type(tmp_corrections)}")    