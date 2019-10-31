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
        super(Square,self).__init__(length,length)

rec = Rectangle(16,4)
print(rec.area())
print(rec.perimeter())


box = Square(5)
print(box.area())
print(box.perimeter())

class Column(Rectangle):
    def __init__(self,length, width):
        super(Column,self).__init__(length,width)
        Area = super(Column,self).area()

    def surface_area(self):
         
        return super(Column,self).area() * 6

    def volume(self):
       
        return super(Column,self).area() * self.length
    
    # def __int(self):
    #     return 

boxy = Column(16,4)
print(boxy.surface_area())
print(boxy.volume())

class A:
    def test(self):
        print("test of A called")

class B(A):
    def test(self):
        print('test of B called')
        super().test()

class C(A):
    def test(self):
        print("test of C called")
        super().test()
class D(B,C):
    def test2(self):
        print("test of D called")

obj = D()
print(obj.test())
# print(obj.test2())        
