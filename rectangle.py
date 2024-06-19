#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle.        

class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return int(self.length) * int(self.width)
  def perimeter(self):
    return 2 * (int(self.length) + int(self.width))
    
rectangle1 = Rectangle("10", "20")
rectangle2 = Rectangle("22" , "39")

print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle2.area())
print(rectangle2.perimeter())
                    
