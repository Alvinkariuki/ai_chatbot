import nltk
from nltk.tokenize import word_tokenize


file = open('random_file.txt')

for line in file:
    seperations = line.split(',')

file.close()

seperations = [s.rstrip('\n') for s in seperations]     #This contains a sentence array
unique_words = []
multi_dim_sep = [s.split(' ') for s in seperations]         #This contains a 2D array of the sentences
multi_dim = [[letter.lower() for letter in multi_word ] for multi_word in multi_dim_sep ]

for ind in multi_dim:
    for speci in ind:
        if speci not in unique_words:
            speci = speci.lower()
            unique_words.append(speci)  #Break down of the non repeating words in the multi_dim array


"""
    Scoring our multi_dim array
"""

score=[]

for word_array in multi_dim:
    bag = []                    #Initialize a temporary array
    i = 0
    for i in range(len(unique_words)):
        if unique_words[i] not in word_array:
            bag.append(0)
            i += 1
        else:
            bag.append(1)
            i += 1
    score.append(bag)           #Fill Score Array with scored values


for _ in range(len(score)):
    print(score[_])
