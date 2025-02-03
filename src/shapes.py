import math

class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r: float):
        self._r = r

    def get_radius(self) -> float:
        return self._r

    def get_area(self) -> float:
        return math.pi * self._r * self._r

    def get_perimeter(self) -> float:
        return 2 * math.pi * self._r
    

class Rectangle(Shape):
    def __init__(self, l: float, w: float):
        self._l = l
        self._w = w

    def __eq__(self, other_rect) -> bool:
        if not isinstance(other_rect, Rectangle):
            return False
        return self._l == other_rect._l and self._w == other_rect._w

    def get_area(self) -> float:
        return self._l * self._w
    
    def get_perimeter(self) -> float:
        return 2 * self._l + 2 * self._w
    

class Square(Rectangle):
    def __init__(self, side_length: int):
        super().__init__(side_length, side_length)