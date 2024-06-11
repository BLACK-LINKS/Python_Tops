a=int(input("Enter A = "))
b=int(input("Enter B = "))
c=int(input("Enter C = "))

if a>b:
    if a>c:
        print("A IS MAX")
    else:
        print("C is Max")
elif b>c:
    print("B is Max")
else:
    print("C is Max")
