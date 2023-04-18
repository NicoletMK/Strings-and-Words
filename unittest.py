from word_frequency import word_statistics

def test_word_statistics():
    # One line sentence w pure Eng words
    assert word_statistics("The quick brown fox jumps over the lazy dog.") == {'word_count': {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}, 'line_count': 1, 'char_count': 36}
    # One sentence with spaces and tabs
    assert word_statistics("The quick\t brown fox\njumps over the\nlazy\t dog.") == {'word_count': {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}, 'line_count': 3, 'char_count': 36}
    # One sentence with numbers and space
    assert word_statistics("The 6th quick brown fox jumps\n over the 1st lazy dog.") == {'word_count': {'the': 2, '6th': 1, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, '1st': 1, 'lazy': 1, 'dog': 1}, 'line_count': 2, 'char_count': 42}
    # Words with multiple spaces
    assert word_statistics("  fox  &    dog") == {'word_count': {'fox': 1, 'dog': 1}, 'line_count': 1, 'char_count': 7}
    # Pure numbers with spaces and tabs
    assert word_statistics("123\n456\t789\n") == {'word_count': {'123': 1, '456': 1, '789': 1}, 'line_count': 2, 'char_count': 9}
    # Empty ducument
    assert word_statistics(" ") == {"word_count":{ }, "line_count": 1, "char_count": 0}


def test_replace(self):
        # Replacement
        document = "The quick\t brown fox\njumps over the\nlazy\t dog."
        result = word_statistics(document, pattern_word='dog', replacement_word='fox')
        self.assertEqual(result['word_count'], {'the': 2, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1})
        self.assertEqual(result['line_count'], 3)
        self.assertEqual(result['char_count'], 36)
        
        # Replacement with \n combination
        document = "The quick\t brown fox\njumps over the\nlazy\t dog."
        result = word_statistics(document, pattern_word='fox', replacement_word='dog')
        self.assertEqual(result['word_count'], {'the': 2, 'quick': 1, 'brown': 1, 'dog': 2, 'jumps': 1, 'over': 1, 'lazy': 1})
        self.assertEqual(result['line_count'], 3)
        self.assertEqual(result['char_count'], 36)
     
        # Replacement with number combination
        document = "The 1st quick\t brown fox\njumps over the\nlazy\t dog."
        result = word_statistics(document, pattern_word='1st', replacement_word='first')
        self.assertEqual(result['word_count'], {'the': 2, 'first': 1, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})
        self.assertEqual(result['line_count'], 3)
        self.assertEqual(result['char_count'], 41)

        # Replacement with spaces
        document = "  fox  &    dog"
        result = word_statistics(document, pattern_word='fox', replacement_word='dog')
        self.assertEqual(result['word_count'], {'dog': 2})
        self.assertEqual(result['line_count'], 1)
        self.assertEqual(result['char_count'], 7)

        # Replacement with numbers
        document = "123\n456\t789\n"
        result = word_statistics(document, pattern_word='123', replacement_word='321')
        self.assertEqual(result['word_count'], {'321': 1, '456': 1, '789': 1})
        self.assertEqual(result['line_count'], 2)
        self.assertEqual(result['char_count'], 9)

        # Replacement when empty
        document = " "
        result = word_statistics(document, pattern_word='fox', replacement_word='dog')
        self.assertEqual(result['word_count'], {})
        self.assertEqual(result['line_count'], 1)
        self.assertEqual(result['char_count'], 0)


# If no test failed
print("All tests passed! Congrats!!")

