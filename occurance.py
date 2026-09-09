n = int(input("Enter number: "))
digit = int(input("Enter digit: "))
count = 0

while n > 0:
    if n % 10 == digit:
        count += 1
    n //= 10

print("Occurrence =", count)