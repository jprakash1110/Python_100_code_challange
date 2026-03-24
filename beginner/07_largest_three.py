# Problem Statement: Find the largest and minimum of three numbers

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter trhe number 2: "))
num3 = int(input("Enter trhe number 3: "))

largerst_number = max(num1, num2, num3)
min_number = min(num1, num2, num3)

print(f'largest number is {largerst_number}')

print(f'lowest number is {min_number}')