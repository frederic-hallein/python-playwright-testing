import pytest
import math

from src import shapes

class TestCircle():
    def setup_method(self, method):
        print(f"\nSetting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"\nTearing down {method}")

    def test_area(self):
        r = 10
        actual = self.circle.get_area()
        expected = math.pi * r * r 
        if actual != expected:
            raise AssertionError(f"Expected A = {expected}, but got A = {actual} instead")