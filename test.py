def is_valid(word: str) -> bool:
    return word.isalpha()


def test():
    assert is_valid("Hello")  == True
    assert is_valid("Hello ") == False
    assert is_valid("Hello:") == False
    assert is_valid("Hello.") == False
    assert is_valid("")       == False
