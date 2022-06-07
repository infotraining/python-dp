import abc
from collections import namedtuple
from typing import List
from dataclasses import dataclass
import logging


@dataclass
class Coord:
    x: int
    y: int

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy


class Shape(abc.ABC):
    @abc.abstractmethod
    def move(self, dx, dy) -> None:
        pass

    @abc.abstractmethod
    def draw(self) -> None:
        pass


class ShapeLogger(Shape):
    def __init__(self, logger, shape):
        self._logger = logger
        self._shape = shape

    def move(self, dx, dy):
        self._shape.move(dx, dy)

    def draw(self):
        self._logger.info('start drawing shape...')
        self._shape.draw()
        self._logger.info('end drawing shape...')


class ShapeBase(Shape):

    def __init__(self, x, y, ):
        self.__coord = Coord(x, y)

    @property
    def coordinates(self) -> Coord:
        return self.__coord

    def move(self, dx, dy) -> None:
        self.__coord.translate(dx, dy)


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

    def move(self, x, y) -> None:
        return self.__rect.move(x, y)


class ShapeGroup(Shape):
    def __init__(self):
        self.__shapes = []

    def add(self, child: Shape):
        self.__shapes.append(child)

    def remove(self, child: Shape):
        self.__shapes.remove(child)

    def draw(self) -> None:
        [sh.draw() for sh in self.__shapes]

    def move(self, dx, dy) -> None:
        [sh.move(dx, dy) for sh in self.__shapes]

    def __iter__(self):
        for i in self.__shapes:
            yield i


def draw_shapes(shapes: ShapeGroup):
    shapes.draw()


if __name__ == "__main__":
    c = Circle(10, 20, 200)
    c.draw()
    c.move(100, 500)
    c.draw()

    print(isinstance(c, Shape))
    print(issubclass(Circle, Shape))

    r = Rectangle(10, 200, 500, 100)
    r.draw()

    s = Square(10, 20, 100)
    s.draw()
    s.size = 400
    s.draw()

    grouped_shapes = ShapeGroup()
    grouped_shapes.add(ShapeLogger(logging, c))
    grouped_shapes.add(ShapeLogger(logging, r))
    grouped_shapes.add(s)
    grouped_shapes.draw()
