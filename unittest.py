from word_frequency import count_words
def test_count_words():
    assert count_words("hello world") == {'hello': 1, 'world': 1}
    assert count_words("Hello, World!") == {'hello': 1, 'world': 1}
    assert count_words("Hello\nWorld") == {'hello': 1, 'world': 1}
    assert count_words("Hello,\t World!") == {'hello': 1, 'world': 1}
    assert count_words("a a a b b c") == {'a': 3, 'b': 2, 'c': 1}
    assert count_words("") == {}
    
test_count_words()
