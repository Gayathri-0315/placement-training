num=int(input("Enter an number:"))
if num < 2:
    print(num,"is not a prime number")
elif num % 2 == 0:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")