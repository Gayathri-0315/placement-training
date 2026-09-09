import math

n = int(input("Enter number: "))
temp = n
s = 0

while n > 0:
    d = n % 10
    s += math.factorial(d)
    n //= 10

if s == temp:
    print("Strong Number")
else:
    print("Not Strong Number")