import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(",")

grades = list(map(int, grades))

min_number = min(grades)

print(min_number)

max_number = max(grades)

print(max_number)

total_value = sum(grades)
total_number = len(grades)
average = round(total_value/total_number, 2)

print(f"the average median number is {average}")

mean = round(statistics.mean(grades),2)
median = statistics.median(grades)

print(f"The max is {max_number}, the min is {min_number}, the mean/average number is {mean}, the median number is {median}")
#print(f"the median number is {median}")
#txt1 = "".format()