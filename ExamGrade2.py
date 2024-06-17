level = int(input("enter a level (1 or 2): "))
grade = int(input("enter a grade: "))

if level == 1:
  if grade >= 71 and grade <= 100:
      print("Distinction")
  elif grade >= 60 and grade <=70:
      print("Merit")
  elif grade >= 50 and grade <= 60:
    print("Pass")
  elif grade <= 49:
    print("Fail")
  else:
    print("Error: marks must be between 1 and 100")
 

if level == 2:
  if grade >= 66 and grade <= 100:
   print("Distinction")
  elif grade >= 51 and grade <=65:
   print("Merit")
  elif grade >= 40 and grade <= 50:
    print("Pass")
  elif grade <= 39:
    print("Fail")
  else:
    print("Error: marks must be between 1 and 100")
