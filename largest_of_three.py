a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>=b and a>=c:
    print(a,"is the largest number")
elif b>=a and b>=c:
    print(b,"is the largest number")
else:
    print(c,"is the largest number")
    