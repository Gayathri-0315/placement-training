n = int(input("Enter number: "))
largest = 0

while n > 0:
    d = n % 10
    if d > largest:
        largest = d
    n //= 10

print("Largest digit =", largest)