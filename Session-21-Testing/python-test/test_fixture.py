# fiture provides reusable test data
# pass it as argument, which guves a fresh copy each time (each test case)
import pytest

@pytest.fixture
def sample_list():
    return [1,2,3]

def test_list_append(sample_list): 
    sample_list.append(4)
    assert sample_list == [1,2,3,4]
    
def test_list_remove(sample_list):
    sample_list.remove(1)
    assert sample_list == [2,3]
    
# let' saye you wnat to run multiple test cases on common data
# everytime not the updated data 
# that common data set with fixture