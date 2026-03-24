# Problen Statement: Take user name and age, print a greeting message

name = input("Enter you name: ")
age = int(input("Enter your age: "))

print(f'Hello {name}, good morning')

if age <= 30:
    print("How are you doing Buddy")

else:
    print("How are you doin sir")