n = int(input("Enter number: "))
temp = n
s = 0
digits = len(str(n))

while n > 0:
    d = n % 10
    s += d ** digits
    n //= 10

if s == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")