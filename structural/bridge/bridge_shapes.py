import abc
from io import StringIO
from typing import List
import turtle

class Drawing(abc.ABC):
    @abc.abstractmethod
    def draw_line(self, x1, y1, x2, y2):
        pass
        
    @abc.abstractmethod
    def draw_circle(self, x, y, r):
        pass

class Shape(abc.ABC):
    @abc.abstractmethod
    def draw():
        pass


class ShapeBase(Shape):
    def __init__(self, drawing: Drawing, x, y):
        self.drawing = drawing
        self.x = x
        self.y = y


class Circle(ShapeBase):
    def __init__(self, drawing, x, y, r):
        super().__init__(drawing, x, y)
        self.r = r
        
    def __repr__(self):
        return 'Circle x={} y={} r={}'.format(self.x, self.y, self.r)
    
    def draw(self):
        self.drawing.draw_circle(self.x, self.y, self.r)


class Rectangle(ShapeBase):
    def __init__(self, drawing, x, y, w, h):
        super().__init__(drawing, x, y)
        self.w = w
        self.h = h
        
    def __repr__(self):
        return 'Rectangle x={} y={} w={} h={}'.format(self.x, self.y, self.w, self.h)
    
    def draw(self):
        x, y, w, h = self.x, self.y, self.w, self.h
        self.drawing.draw_line(x  , y  , x+w, y  )
        self.drawing.draw_line(x  , y  , x  , y+h)
        self.drawing.draw_line(x+w, y  , x+w, y+h)
        self.drawing.draw_line(x  , y+h, x+w, y+h)
    
class Square(Shape):
    def __new__(cls, drawing, x, y, a):
        return Rectangle(drawing, x, y, a, a)


class TurtleDrawing(Drawing):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        turtle.resetscreen()
        turtle.penup()
        
    def draw_line(self, x1, y1, x2, y2):
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)
        turtle.penup()
    
    def draw_circle(self, x, y, r):
        turtle.goto(x, y-r)
        turtle.pendown()
        turtle.circle(r)
        turtle.penup()


class ConsoleDrawning(Drawing):
    def draw_line(self, x1, y1, x2, y2):
        print(f"Line from ({x1}, {y1}) to ({x2}, {y2})")
    
    def draw_circle(self, x, y, r):
        print(f"Circle at ({x},{y}) - radius: {r}")

if __name__ == "__main__":
    #drawing = TurtleDrawing()
    drawing = ConsoleDrawning()

    shapes = [Circle(drawing, 50, 50, 50), Rectangle(drawing, 40, 20, 100, 200)]

    for s in shapes:
        s.draw()