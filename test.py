attempts = 0
max_attempts = 3

while attempts < max_attempts:
  # Your code that asks the user for input
  # ... 
  # Your code that checks if the input is correct
  # ...
  if input_is_correct:
    # Success, exit the loop
    break
  else:
    attempts += 1
    print(f"Incorrect. You have {max_attempts - attempts} attempts left.")

if attempts == max_attempts:
  print("None")