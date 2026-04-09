# Problem Statement: Check if a number is prime or composite

num = int(input("Enter the number to check if it is prime: "))

if num <= 1:
    print(f"{num} is not prime or composite")

else:

    for n in range (2, num):
        if num % n == 0:
            print(f"{num}, is composite number")
            break

        else:
            print(f"{num}, is prime number")