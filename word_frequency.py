import re

def word_statistics(document):
    word_dict = {}
    words = re.findall(r'\w+', document)
    for word in words:
        if word.lower() in word_dict:
            word_dict[word.lower()] += 1
        else:
            word_dict[word.lower()] = 1
            
    line_count = len(document.splitlines())

    separators = [' ', '\t', '\n']
    for separator in separators:
        document = document.replace(separator, '')
    char_count = len(document)

    return {"word_count": word_dict, "line_count": line_count, "char_count": char_count}
