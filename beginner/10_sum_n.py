# Problem Statement: Print sum of first N natural numbers

num = int(input("Eneter a number: "))

if num <= 0:
    print("Enter a positive number")

sum_n = num * (num +1) / 2

print(f' sum of first n natiral number is: {sum_n}')