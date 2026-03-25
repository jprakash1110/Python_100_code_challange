# Problem Statement: Print multiplication table of a number
num = int(input("Enter the number: "))
table = 0
for n in range (1, 11):
    table = num * n
    print(f'{num} * {n} = {table}')