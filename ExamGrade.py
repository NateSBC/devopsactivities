grade = int(input("enter a grade: "))
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
  