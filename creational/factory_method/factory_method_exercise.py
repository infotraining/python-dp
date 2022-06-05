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
        print('Rectangle x={} y={} w={} h={}'.format(self.x, self.y, self.w, self.h))


class Drawing:
    def __init__(self, shapes):
        self._shapes = shapes

    def __repr__(self):
        return '<Drawing {}>'.format(str(self._shapes))

    @classmethod
    def from_stream(cls, stream):
        shapes = []
        for line in stream:
            line = line.strip()
            if not line:
                continue
            shape_name, *parameters = line.split()
            parameters = map(int, parameters)
            if shape_name == 'Circle':
                shape = Circle(*parameters)
            elif shape_name == 'Rectangle':
                shape = Rectangle(*parameters)
            elif shape_name == 'Square':
                x, y, a = parameters
                shape = Rectangle(x, y, a, a)
            else:
                raise TypeError
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
