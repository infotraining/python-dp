from io import StringIO


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def draw(self):
        print('Circle x={} y={} r={}'.format(self.x, self.y, self.r))


class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def draw(self):
        print('Rectangle x={} y={} w={} h={}'.format(
            self.x, self.y, self.w, self.h))


shape_factory = {'Circle': Circle, 'Rectangle': Rectangle,
                 'Square': lambda x, y, size: Rectangle(x, y, size, size)}


class Drawing:
    def __init__(self, shapes):
        self._shapes = shapes

    def __repr__(self):
        return '<Drawing {}>'.format(str(self._shapes))

    @classmethod
    def from_stream(cls, stream, shape_factory=shape_factory):
        shapes = []
        for line in stream:
            line = line.strip()
            if not line:
                continue
            shape_name, *parameters = line.split()
            parameters = map(int, parameters)

            shape = shape_factory[shape_name](*parameters)
            shapes.append(shape)
        return cls(shapes)

    def render(self):
        for s in self._shapes:
            s.draw()


if __name__ == "__main__":

    raw_shapes = '''
Circle 15 10 14
Rectangle 30 30 100 150
Circle 40 20 5
Square 30 100 20
'''

    graphics = Drawing.from_stream(StringIO(raw_shapes))
    graphics.render()
