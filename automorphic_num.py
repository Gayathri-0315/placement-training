n = int(input("Enter number: "))

if str(n * n).endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not Automorphic Number")