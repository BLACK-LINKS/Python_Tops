rno=int(input("Enter roll no : "))
sname=input("Enter Student Name : ")
s1=int(input("English marks : "))
s2=int(input("Science marks : "))
s3=int(input("Maths marks : "))

total=s1+s2+s3
per=total/3

print("Roll no : ", rno)
print("Name : ", sname)
print("Total marks : ", total)
print("Percentage : ", per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("First class")
elif per>=50:
    print("Second class")
elif per>=40:
    print("Pass")
else:
    print("Fail")
