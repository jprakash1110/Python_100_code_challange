# Problem Statement: Check if a number is positive, negative, or zero

num = int(input("Enter the number: "))

if num > 0:
    print(f'{num} is positive number')

elif num == 0:
    print(f'{num} is nither positive nor negative it is {num}')

else:
    print(f'{num} is nigative number')