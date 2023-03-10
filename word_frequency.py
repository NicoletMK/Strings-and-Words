import re

def count_words(document):
    word_dict = {}
    words = re.findall(r'\w+', document)
    for word in words:
        if word.lower() in word_dict:
            word_dict[word.lower()] += 1
        else:
            word_dict[word.lower()] = 1
    return word_dict
