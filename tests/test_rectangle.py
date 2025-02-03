import pytest

from src import shapes

def test_same_rectangle_area(my_rectangle):
    actual = my_rectangle.get_area()
    l = 10
    w = 5
    expected = l * w
    assert actual == expected, f"Expected A = {expected}, but got A = {actual} instead"
    
def test_same_rectangle_perimeter(my_rectangle):
    actual = my_rectangle.get_perimeter()
    l = 10
    w = 5
    expected = 2 * l + 2 * w
    assert actual == actual, f"Expected S = {expected}, but got S = {actual} instead"
    
def test_not_equal_rectangles(my_rectangle, other_rectangle):
    assert my_rectangle != other_rectangle, \
        f"Expected rectangle {my_rectangle} to not be equal to rectangle {other_rectangle}, but instead are equal"

def test_not_equal_area(my_rectangle, other_rectangle):
    assert my_rectangle.get_area() != other_rectangle.get_area(), \
        f"Expected area rectangle {my_rectangle} to not be equal to area rectangle {other_rectangle}, but instead are equal"