print("Welcome to this calculator app! Enter the operator you want to use by choosing the corresponding number... ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")

while True:
    operator = input("Enter operator option: ")

    if operator in ('1', '2', '3', '4', '5'):
        firstnum = float(input("Enter first number: "))
        secondnum = float(input("Enter second number: "))

        if operator == '1':
            print(firstnum, "+", secondnum, "=", firstnum + secondnum)

        elif operator == '2':
            print(firstnum, "-", secondnum, "=", firstnum - secondnum)

        elif operator == '3':
            print(firstnum, "x", secondnum, "=", firstnum * secondnum)

        elif operator == '4':
            print(firstnum, "/", secondnum, "=", firstnum / secondnum)

        elif operator == '5':
            print(firstnum, "^", secondnum, "=", firstnum ** secondnum)

        break
    else:
        print("Invalid Input")
