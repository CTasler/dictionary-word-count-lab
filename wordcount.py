"""Count words in file."""

from string import punctuation
import sys
import string


file = open(sys.argv[1])

def tokenize(file):
    words = []
    for line in file: 
        line = line.rstrip().split(" ")
        for word in line: 
            word = word.translate(str.maketrans(" "," ", string.punctuation))
            #replaces all punctuation in word with None
            word = word.title()
            words.append(word)
    return words


def count_words(words):
    word_count = {}
    for word in words: 
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
    
    
def print_word_count(word_count):
    for word, count in word_count.items():
        print(word, count)


print_word_count(count_words(tokenize(file)))

"""Can write above code as below:
tokens = tokenize(filename)
word_count = count_words(words)
print_word_count(word_count)
"""