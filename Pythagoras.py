print("Pythagoras’ Calculator \n1. Find the length of A given B and C  \n2. Find the length of B given A and C  \n3. Find the length of C given A and B")

py = int(input("Enter option: "))

if py == 1:
  b = int(input("Enter length of B: "))
  c = int(input("Enter length of C: "))
  a = (c**2 + b**2)**0.5
  print("The length of A is", a)
elif py == 2:
  a = int(input("Enter length of A: "))
  c = int(input("Enter length of C: "))
  b = (c**2 + a**2)**0.5
  print("The length of B is", b)
elif py == 3:
  a = int(input("Enter length of A: "))
  b = int(input("Enter length of B: "))
  c = (c**2 + a**2)**0.5
  print("The length of C is", c)