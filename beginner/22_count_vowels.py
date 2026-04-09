# Problem Statemen: Count vowels in a string

word = input("Enter a word: ").lower()

vowel = ["a", "e", "i", "o", "u"]

count = 0
for i in word:
    if i in vowel:
        count += 1
print(count)