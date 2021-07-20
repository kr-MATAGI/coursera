get_ratio(freqs, 'happi')

def get_ratio(freqs, word):
    '''
    Input:
        freqs: dictionary containing the words
        word: string to lookup

    Output: a dictionary with keys 'positive', 'negative', and 'ratio'.
        Example: {'positive': 10, 'negative': 20, 'ratio': 0.5}
    '''
    pos_neg_ratio = {'positive': 0, 'negative': 0, 'ratio': 0.0}
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    # use lookup() to find positive counts for the word (denoted by the integer 1)
    pos_neg_ratio['positive'] = freqs.get((word, 1.0), 0)

    # use lookup() to find negative counts for the word (denoted by integer 0)
    pos_neg_ratio['negative'] = freqs.get((word, 0.0), 1)

    # calculate the ratio of positive to negative counts for the word
    pos_neg_ratio['ratio'] = pos_neg_ratio['positive'] / pos_neg_ratio['negative']
    ### END CODE HERE ###
    return pos_neg_ratio