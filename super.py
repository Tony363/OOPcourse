class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

rec = Rectangle(16,4)
print(rec.area())
print(rec.perimeter())

box = Square(5)
print(box.area())
print(box.perimeter())
