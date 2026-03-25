# Problem Statement: Check if a number is palindrome

num = int(input("Enter the number: "))

if num > 0:
    rev_num = str(num) [::-1]
    if str(rev_num) == str(num):
        print(f"Number you have entered is palindrome, and number is {num}")
    else:
        print(f"Number you have entered is not palindrome, and number is {num}")

elif num == 0:
    print("Please enter a valid +ve or -ve integer")