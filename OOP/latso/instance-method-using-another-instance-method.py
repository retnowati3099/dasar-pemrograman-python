class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(20, 30)
print(rectangle1.area())
print(rectangle1.perimeter())
'''
Create a class Rectangle with attributes length and width. Define an instance method area that returns the area of the rectangle. Definea another instance method perimeter that returns the perimeter of the rectangle!
'''