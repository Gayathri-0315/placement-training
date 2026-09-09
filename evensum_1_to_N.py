n = int(input("Enter N: "))
s = 0

for i in range(2, n + 1, 2):
    s += i

print("Sum =", s)