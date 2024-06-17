number = int(input("Enter a number: ")) # The number we want the factorial of
factorial = 1 # Start with 1, as anything multiplied by 1 is itself
i = 1 # Counter for the loop
while i <= number: # Keep going while 'i' is less than or equal to 'number'
  factorial = factorial * i # Multiply the 'factorial' by 'i'
  i = i + 1 # Increase 'i' for the next multiplication
print(factorial) # Print the final result