# Problem Statement: Generate Fibonacci series up to N terms

num = int(input("Enter a number up to younwant to generate fibonacci: "))
a = 0
b = 1
series = [a, b]
for n in range(1, num+1):
    c = a + b
    a = b
    b = c
    series.append(c)
print(series)