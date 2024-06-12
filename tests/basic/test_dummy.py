import pytest

def test_dummy_1():
    pass

def test_dummy_2():
    pass

def test_dummy_3():
    pass

@pytest.mark.parametrize("a", [1,2,3])
def test_parametrized_dummy(a):
    pass
