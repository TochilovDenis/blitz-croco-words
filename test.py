def is_valid(word: str) -> bool:
    return word.isalpha()


def test():
    assert is_valid("Hello")  == True
    assert is_valid("Hello ") == False
    assert is_valid("Hello:") == False
    assert is_valid("Hello.") == False
    assert is_valid("")       == False


def test_all_word():
    with open("words.txt", 'r', encoding="UTF-8") as file:
       for word in file:
            assert is_valid(word.strip()) == True


