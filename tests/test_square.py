import pytest

from src import shapes

@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (10, 100), (1, 1)])
def test_multiple_square_areas(side_length, expected_area):
    actual = shapes.Square(side_length).get_area()
    assert actual == expected_area, \
        f"Expected A = {expected_area}, but got A = {actual}"
    


@pytest.mark.parametrize("side_length, expected_perimeter", [(5, 20), (10, 40), (1, 4)])
def test_multiple_square_perimeter(side_length, expected_perimeter):
    actual = shapes.Square(side_length).get_perimeter()
    assert actual == expected_perimeter, \
        f"Expected S = {expected_perimeter}, but got S = {actual}"