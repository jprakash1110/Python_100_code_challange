# Problem Statement: Find factorial of a number

num = int(input("Enter the number: "))
factorial = 1

if num < 0:
    print("Factorial can be calculated for +ve interger")

elif num == 0:
    print("Factorial of 0 is 1")

else:
    for n in range(1, num + 1):
        factorial *= n
        print(f'{n}! = {factorial}')