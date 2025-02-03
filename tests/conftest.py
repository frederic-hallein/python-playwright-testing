import pytest
from src import shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 5)

@pytest.fixture
def other_rectangle():
    return shapes.Rectangle(20, 2)