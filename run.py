from word_frequency import word_statistics

# One line sentence w pure Eng words
document = "The quick brown fox jumps over the lazy dog."
result = word_statistics(document)
print(result)

# One sentence with spaces and tabs
document = "The quick\t brown fox\njumps over the\nlazy\t dog."
result = word_statistics(document)
print(result)

# One sentence with numbers and space
document = "The 6th quick brown fox jumps\nover the 1st lazy dog."
result = word_statistics(document)
print(result)

# Words with multiple spaces
document = "  fox  &    dog"
result = word_statistics(document)
print(result)

# Pure numbers with spaces and tabs
document = "123\n456\t789\n"
result = word_statistics(document)
print(result)

# Empty ducument
document = " "
result = word_statistics(document)
print(result)

# Replacement
document = "The quick\t brown fox\njumps over the\nlazy\t dog."
result = word_statistics(document, pattern_word='dog', replacement_word='fox')
print(result)

# Replacement with \n combination
document = "The quick\t brown fox\njumps over the\nlazy\t dog."
result = word_statistics(document, pattern_word='fox', replacement_word='dog')
print(result)

# Replacement with number combination
document = "The 1st quick\t brown fox\njumps over the\nlazy\t dog."
result = word_statistics(document, pattern_word='1st', replacement_word='first')
print(result)

# Replacement with spaces
document = "  fox  &    dog"
result = word_statistics(document, pattern_word='fox', replacement_word='dog')
print(result)

# Replacement with numbers
document = "123\n456\t789\n"
result = word_statistics(document, pattern_word='123', replacement_word='321')
print(result)

# Replacement when empty
document = " "
result = word_statistics(document, pattern_word='fox', replacement_word='dog')
print(result)
        