def get_document_embedding(tweet, en_embeddings): 
    '''
    Input:
        - tweet: a string
        - en_embeddings: a dictionary of word embeddings
    Output:
        - doc_embedding: sum of all word embeddings in the tweet
    '''
    doc_embedding = np.zeros(300)

    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    # process the document into a list of words (process the tweet)
    processed_doc = process_tweet(tweet)
    
    for word in processed_doc:
        # add the word embedding to the running total for the document embedding
        doc_embedding = doc_embedding + en_embeddings.get(word, 0)
    ### END CODE HERE ###
    return doc_embedding