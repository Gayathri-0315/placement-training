n = int(input("Enter number: "))
rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n //= 10

print("Reverse =", rev)