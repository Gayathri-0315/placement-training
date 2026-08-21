num=int(input("Enter a number:"))
if num % 5 == 0 and num % 11 == 0:
    print(num,"is divisible by both 5 and 11")
else:
    print(num, "is not divisible by both 5 and 11")