#Part 1
#Create a Student class that takes the name and age on creation.
#Create 2 objects of your student class and get the age of one of them.


class Student:
       def __init__(self, first, last, age, classroom, *grades): 
         self.first = first  
         self.last = last 
         self.age = age
         self.classroom = classroom
         self.grades = []
  
       def fullname(self):
         return self.first + " " + self.last

       def change_classroom(self, new_classroom):
              self.classroom = new_classroom

       def add_grade(self, *grade):
              self.grades.append(grade)
              
              
student1 = Student("john", "smith", 10, "maths")
student2 = Student("katy", "smith", 12, "english")

student1.add_grade(0, 50, 100)

print(student1.first, student1.age, student1.classroom)
print(student2.first, student2.age, student2.classroom)
student2.change_classroom("science")

print(student2.classroom)
print(student1.grades)

student1_grade = int(sum(student1.grades))

print (student1_grade)
