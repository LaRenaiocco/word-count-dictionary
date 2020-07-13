import sys
text_file = sys.argv[1]

def make_word_count_dictionary(text_file):
    words_to_count = open(text_file)

    word_count = {}
    punctuation_tuple = ('.', ',', '!', '?', '"', ':', ';', '(', ')')

    for line in words_to_count:
        line = line.strip()
        #print(line)
        words = line.split(' ')
        #print(words)
        for word in words:
            word = word.lower().strip()
            # for letter in word:
            #     if letter == '.' or letter == ',':
            #         word.pop(letter)
            if word.endswith(punctuation_tuple) or word.startswith(punctuation_tuple):
                #print(word)
                char_list = []
                for char in word:
                    if char not in punctuation_tuple:
                        char_list.append(char)
                #print(char_list)
                word = ''.join(char_list)
                # for char in word:
                #     char.pop()
            #     for index, letter in enumerate(word):
            #         word.pop(-1)
            #if word[-1] == '.':
                #word.pop(-1)
            word_count[word] = word_count.get(word, 0) + 1


        #adds each letter to dictionary
        # for word in line:
        #     word_count[word] = word_count.get(word, 0) + 1

    for k, v in word_count.items():
        print(k, v)

make_word_count_dictionary(text_file)



