import pytest

square = lambda x: x ** 2
cube = lambda x: x ** 3
fifth_power = lambda x: x ** 5

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(0) == 0

def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(0) == 0

def test_fifth_power():
    assert fifth_power(2) == 32
    assert fifth_power(3) == 243
    assert fifth_power(0) == 0

def test_wrong_input(): 
    with pytest.raises(TypeError):
        square("a")
    with pytest.raises(TypeError):
        cube("a")
    with pytest.raises(TypeError):
        fifth_power("a")
