import csv

companies = []
sales = []

with open("output.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    for row in reader:
        companies.append(row[0].replace(",",""))
        #sales.append(float(row[1].replace(",","")))
        sales.append(int(row[1].replace(",","")))

#monthly_sum = [sum(x) for x in sales] 

print(companies)
print(sales)
