import pytest
from calculator import add, sub, mul, div

def test_add():
    assert add(2,3)==5 
    assert add(-1,1)==0
    assert add(0,0)==0
    # add(2,3) actual value, 5 is expected
    
def test_sub():
    assert sub(5,3)==2
    assert sub(0,4)==-4
    assert sub(-1,1)==-2
    
## write test case for div and mul

def test_div_zero():
    with pytest.raises(ValueError):
        div(2,0)
        
## How to run?
# setup virtual environment
# python -m venv venv (in wsl python3 -m venv venv)
# activate: venv\Scripts\activate
# pip install pytest
# just run: pytest 
# it will detect all test case files start with test_*.py name