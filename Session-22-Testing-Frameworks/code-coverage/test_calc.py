import pytest
from calculator import add,sub,mul,div

def test_add():
    assert add(2,3)==5
def test_sub():
    assert sub(2,3)==-1
def test_mul():
    assert mul(2,3)==6
def test_div():
    assert div(10,2)==5
    
# python -m venv venv
# venv\Scripts\activate
# pip install pytest coverage
# coverage run -m pytest
# coverage report
# coverage html (check generated htmlcov folder open index.html and see result)

# Code coverage using pytest-cov
# pip install pytest pytest-cov
# pytest --cov=calculator
# pytest --cov=calculator --cov-report=html
# generated folder htmlcov --> check index.html