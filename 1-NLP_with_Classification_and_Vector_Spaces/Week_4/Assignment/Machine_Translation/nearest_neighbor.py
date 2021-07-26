def nearest_neighbor(v, candidates, k=1):
    """
    Input:
      - v, the vector you are going find the nearest neighbor for
      - candidates: a set of vectors where we will find the neighbors
      - k: top k nearest neighbors to find
    Output:
      - k_idx: the indices of the top k closest vectors in sorted form
    """
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    similarity_l = []

    # for each candidate vector...
    for row in candidates:
        # get the cosine similarity
        cos_similarity = cosine_similarity(row, v)

        # append the similarity to the list
        similarity_l.append(cos_similarity)
        
    # sort the similarity list and get the indices of the sorted list
    sorted_ids = np.argsort(similarity_l)
    
    # get the indices of the k most similar candidate vectors
    k_idx = sorted_ids[-k:]
    ### END CODE HERE ###
    return k_idx