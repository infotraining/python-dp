import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius


class Rectangle(Shape):

    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height


class Line(Shape):

    def __init__(self, x, y, endx, endy):
        super().__init__(x, y)
        self.endx = endx
        self.endy = endy


def _qualname(obj):
    """Get the fully-qualified name of an object (including module)"""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj: object):
    """Get the name of the class that declared an object"""
    name = _qualname(obj)
    return name[:name.rfind('.')]


# stores the actual visitor methods
_methods = {}


# delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor implementation"""
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)


# visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method"""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator


class AreaVisitor:

    @visitor(Circle)
    def visit(self, circle):
        return math.pi * (circle.radius ** 2)

    @visitor(Rectangle)
    def visit(self, rect):
        return rect.width * rect.height

    @visitor(Line)
    def visit(self, line):
        return 0


def main():
    shapes = [Circle(1, 10, 10), Rectangle(5, 6, 20, 2), Line(54, 23, 100, 300)]

    area_visitor = AreaVisitor()

    areas = [area_visitor.visit(s) for s in shapes]

    print("areas = {}".format(areas))

if __name__ == '__main__':
    main()