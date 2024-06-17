
# 2. Ask the user to input an integer.
# 3. Display the number&#39;s factorial using a while loop.
# Note: the factorial of a number is that number multiplied by all the preceding
# numbers.

# The factorial of 5 is = 5 x 4 x 3 x 2 x 1 = 120
# or if you like = 1

user_number = int(input("Enter a number: "))
fact = 1
counter = 1

while counter <= user_number:
  fact = fact * counter
  counter += 1
print(fact)