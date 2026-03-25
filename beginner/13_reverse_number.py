# Problem statement: Reverse a number

num = int(input("Enter the number: "))

if num > 0:
    rev_num = str(num) [::-1]
    print(f'Original Number: {num}, Revrersed number is: {rev_num}')

elif num == 0:
    print("Please enter a +ve or -ve interger")

else:
    rev_num = (str(abs(num))) [::-1]
    print(f'Original Number: {num}, Revrersed number is: -{rev_num}')