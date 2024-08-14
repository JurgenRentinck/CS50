from hello import hello
import pytest



def test_argument():
    assert hello("David") == "Hello, David"

def test_default():
    assert hello() == "Hello, world"