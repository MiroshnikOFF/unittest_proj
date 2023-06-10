import pytest
from utils import arrs

@pytest.fixture
def array():
    return [1, 2, 3, 4]

def test_get(array):
    assert arrs.get(array, 1, "test") == 2
    assert arrs.get(array, 0, "test") == 1
    assert arrs.get(array, -2, "test") == "test"

def test_slice(array):
    assert arrs.my_slice(array, 1, 3) == [2, 3]
    assert arrs.my_slice(array, 1) == [2, 3, 4]
    assert arrs.my_slice([], 2, 4) == []
    assert arrs.my_slice(array, -2, 3) == [3]
    assert arrs.my_slice(array, -5, 3) == [1, 2, 3]
