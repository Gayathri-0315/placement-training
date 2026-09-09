n = int(input("Enter number: "))
smallest = 9

while n > 0:
    d = n % 10
    if d < smallest:
        smallest = d
    n //= 10

print("Smallest digit =", smallest)