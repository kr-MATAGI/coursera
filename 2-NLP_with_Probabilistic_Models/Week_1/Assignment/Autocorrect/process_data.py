# UNQ_C1 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: process_data
def process_data(file_name):
    """
    Input: 
        A file_name which is found in your current directory. You just have to read it in. 
    Output: 
        words: a list containing all the words in the corpus (text file you read) in lower case. 
    """
    words = [] # return this variable correctly

    ### START CODE HERE ###         
    regex = re.compile("\w+")    
    with open(file_name, 'r') as file:
        while True:
            line = file.readline()
            if not line: break

            line = str(line.strip()).replace('b\'', '').lower()
            line = regex.findall(line)
            for item in line: words.append(item)
                                             
    ### END CODE HERE ###
    
    return words
    
#DO NOT MODIFY THIS CELL
word_l = process_data('shakespeare.txt')
vocab = set(word_l)  # this will be your new vocabulary
print(f"The first ten words in the text are: \n{word_l[0:10]}")
print(f"There are {len(vocab)} unique words in the vocabulary.")