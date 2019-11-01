class Rectangle:
    def __init__(self, length, width):
        self.length = length*100
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square,self).__init__(length,length+1)
        print(self.width)
        length = length + 4


class Square2():
    def __init__(self, length):
        self.length = length
        self.width = length


rec = Rectangle(16,4)
print(rec.area())
print(rec.perimeter())
Square(4)


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
    def test2(self):
        print("super of class A was tested")
class B(A):
    def test(self):
        print('test of B called')
        super().test()
        print('class B super was tested')
        super().test2()
        
class C(A):
    def test(self):
        print("test of C called")
        super().test()
        print('class C super was tested')
        super().test2()
class D(B,C):
    def test2(self):
        print("test of D called")
obj = D()
obj.test()
# obj.test2()   


class A1:
    def __init__(self):
        self.multiply(15)
        print(self.i)
    
    def multiply(self, i):
        self.i = 4*i

class B1(A1):
    def __init__(self):
        super().__init__()

    def multiply(self,i):
        self.i = 2 * i
obj1 = B1()
print(obj1)

class stud:
    def __init__(self, roll_no,grade):
        self.roll_no = roll_no
        self.grade = grade
    def display(self):
        print("Roll no:", self.roll_no, ",Grade:", self.grade)

stud1 = stud(34,"S")
stud1.age=7
print(hasattr(stud1,"age"))