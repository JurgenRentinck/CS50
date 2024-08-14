from calculator import square
import pytest

#def test_square():
    #if square(2) != 4:
    #    print("2 square is not 4!")
    #if square(3) != 9:
    #    print("3 square is not 9!")        
    #try:
    #    assert square(2) == 4
    #    assert square(3) == 9
    #except AssertionError:
    #    pass

#def test_square():
#    assert square(2) == 4
#    assert square(3) == 9
#    assert square(-2) == 4
#    assert square(-3) == 9
#    assert square(0) == 0

#pip install pytest, run script with pytest on commandline
# like this pytest test_calculator.py

def test_positive():
    assert square(2) == 4
    assert square(3) == 9    

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")