# UNQ_C10
# GRADED FUNCTION
def mbr_decode(sentence, n_samples, score_fn, similarity_fn, NMTAttn=None, temperature=0.6, vocab_file=None, vocab_dir=None):
    """Returns the translated sentence using Minimum Bayes Risk decoding

    Args:
        sentence (str): sentence to translate.
        n_samples (int): number of samples to generate
        score_fn (function): function that generates the score for each sample
        similarity_fn (function): function used to compute the overlap between a pair of samples
        NMTAttn (tl.Serial): An LSTM sequence-to-sequence model with attention.
        temperature (float): parameter for sampling ranging from 0.0 to 1.0.
            0.0: same as argmax, always pick the most probable token
            1.0: sampling from the distribution (can sometimes say random things)
        vocab_file (str): filename of the vocabulary
        vocab_dir (str): path to the vocabulary file

    Returns:
        str: the translated sentence
    """
    
    ### START CODE HERE (REPLACE INSTANCES OF `None` WITH YOUR CODE) ###
    # generate samples
    samples, log_probs = generate_samples(sentence, n_samples, temperature, vocab_file, vocab_dir)
    
    # use the scoring function to get a dictionary of scores
    # pass in the relevant parameters as shown in the function definition of 
    # the mean methods you developed earlier
    scores = similarity_fn(similarity_fn, samples, log_probs)
    
    # find the key with the highest score
    max_index = max(scores, key=scores.get)
    
    # detokenize the token list associated with the max_index
    translated_sentence = detokenize(samples[max_index], vocab_file, vocab_dir)
    
    ### END CODE HERE ###
    return (translated_sentence, max_index, scores)