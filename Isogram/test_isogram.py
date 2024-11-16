from is_isogram import is_isogram

def test_isogram():
    assert is_isogram('') == True
    assert is_isogram("isogram") == True
    assert is_isogram("eleven") == False
    assert is_isogram("zzyzx") == False
    assert is_isogram("subdermatoglyphic") == True
    assert is_isogram('"angola"') == False
    assert is_isogram('dave1212') == True
