n = int(input("Enter number: "))
square = n * n
s = 0

while square > 0:
    s += square % 10
    square //= 10

if s == n:
    print("Neon Number")
else:
    print("Not Neon Number")