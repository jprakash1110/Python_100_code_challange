# Take two numbers and print sum, difference, product, division

ch = int(input("Please select what to perform \n 1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Division \n"))
a = int(input("Enter numbaer 1: "))
b = int(input("Enter number 2: "))

#Adding the numbers
if ch == 1:
    print(f'{a} + {b} = {a + b}')

#Subtracting the numbers
elif ch == 2:
    print(f'{a} - {b} = {a - b}')

#Multiplying the numbers
elif ch == 3:
    print(f'{a} * {b} = {a * b}')

#Dividing the numbers
else:
    print(f'{a} / {b} = {a / b}')