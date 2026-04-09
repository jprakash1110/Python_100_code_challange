# Problem Statement: Take a character and check if it is a vowel

alpha = input("Enter a character to check if it is a vowel: ").lower()

vowel = ["a", "e", "i", "o", "u"]

for i in vowel:
    if len(alpha) != 1:
        print("Please enter exactly one character")
        break

    elif alpha == i:
        print(f'{alpha} is a vowel')
        break
else:
    print(f'{alpha} is not a vowel')