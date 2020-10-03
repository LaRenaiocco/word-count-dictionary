#task: import a string of words from a file and create a dictionary that keeps
#track of word count.

import sys
from collections import Counter
text_file = sys.argv[1]

def make_word_count_dictionary(text_file):
    file = open(text_file).read()
    words_list = file.split()
    word_count_dict = {}
    for word in words_list:
        word = word.lower()
        #strip end punctiation from a word
        if not word[-1].isalpha():
            end = word[-1]
            word = word.strip(end)
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict

words = make_word_count_dictionary(text_file)

def print_word_count(words):
    for key, value in words.items():
        print(key, value)

print_word_count(words)