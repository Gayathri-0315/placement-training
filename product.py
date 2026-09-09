n = int(input("Enter number: "))
p = 1

while n > 0:
    p *= n % 10
    n //= 10

print("Product =", p)