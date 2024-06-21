print("START CODE")

try:
    a=int(input("Enter A : "))
    b=int(input("Enter B : "))
    c=a/b
    print("Division : ", c)
    l=[1,2,3,4,5]
    index=int(input("Enter Index Nmuber: "))
    print(l[index])
except Exception as e:
    print("Exception caught : ", e)

print("End Code")    
