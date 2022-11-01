# Given two numbers keep adding 1 to each number until the sum of their squares exceeds 90

a = 1
b = 2

while a**2 + b**2 < 90:
    a = a+1
    b = b+1

print(a, b)