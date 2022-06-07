import abc
from collections import namedtuple
from typing import List

Coord = namedtuple('Coord', 'x,y')


class Shape(abc.ABC):

    @abc.abstractproperty
    def coordinates(self) -> Coord:
        pass

    @abc.abstractmethod
    def move_to(self, x, y) -> None:
        pass

    @abc.abstractmethod
    def draw(self) -> None:
        pass


class ShapeBase(Shape):
    def __init__(self, x, y, ):
        self.__coord = Coord(x, y)

    @property
    def coordinates(self) -> Coord:
        return self.__coord

    def move_to(self, x, y) -> None:
        self.__coord = Coord(x, y)


class Circle(ShapeBase):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.__radius = r

    def draw(self) -> None:
        print(f'Circle at {self.coordinates} with radius {self.__radius}')


class Rectangle(ShapeBase):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.__width = w
        self.__height = h

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        self.__width = new_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    def draw(self) -> None:
        print(
            f'Rectangle at {self.coordinates} with width={self.__width} & height={self.__height}')


class Square(Shape):
    def __init__(self, x, y, size):
        self.__rect = Rectangle(x, y, size, size)

    @property
    def size(self):
        return self.__rect.width

    @size.setter
    def size(self, new_size):
        self.__rect.width = new_size
        self.__rect.height = new_size

    @property
    def coordinates(self) -> Coord:
        return self.__rect.coordinates

    def draw(self):
        self.__rect.draw()

    def move_to(self, x, y) -> None:
        return self.__rect.move_to(x, y)


def draw_shapes(shapes: List[Shape]):
    for s in shapes:
        s.draw()


if __name__ == "__main__":
    c = Circle(10, 20, 200)
    c.draw()
    c.move_to(100, 500)
    c.draw()

    print(isinstance(c, Shape))
    print(issubclass(Circle, Shape))

    r = Rectangle(10, 200, 500, 100)
    r.draw()

    s = Square(10, 20, 100)
    s.draw()
    s.size = 400
    s.draw()
