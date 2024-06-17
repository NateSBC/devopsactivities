# Add a new file: Investment.py and make it the startup file.
# 2. Calculates how many years it will take an initial investment of £100 to grow to a
# target value of £1000 if the interest rate is 10%.
# Tip: Do not start writing code until you&#39;ve a plan of action!
# 3. Save and run.

# 2

# 4. Make your calculation more usable by inputting the following values:

# Initial investment

# Target value
# Interest rate
# 5. Save and run.

# years = 1
# investment = 100
# target = 1000
# rate = 10

# while investment < target:
#   investment = investment + (investment / rate)
#   years += 1

# print(investment)
# print(years)

years = 1
investment = int(input("Enter a initial investment amount: "))
target = int(input("Enter a target value: "))
rate = int(input("Enter a interest rate: "))

while investment < target:
  investment = investment + (investment / rate)
  years += 1

print(f"Final investment total = £{investment}")
print(f"Years = {years}")