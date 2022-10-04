"""Count words in file."""


# put your code here.
from string import punctuation
import sys
import string


file = open(sys.argv[1])

def print_word_count(file):
    words = []
    word_count = {}
    punctuation_marks = [',', '.', ':', ';', '"', '--', '?']
    for line in file: 
        line = line.rstrip().split(" ")
        for word in line: 
            word = word.translate(str.maketrans(" "," ", string.punctuation))
            word = word.title()
            words.append(word)
    for word in words: 
        word_count[word] = word_count.get(word, 0) + 1
    for word, count in word_count.items():
        print(word, count)


print_word_count(file)