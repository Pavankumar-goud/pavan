from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(1,2)==3

def test_sub():
    assert sub(3,2)==1
    assert sub(3,3)==0

