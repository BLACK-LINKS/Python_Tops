t=(1,2,3,4,5,"JAVA",[10,20,30])

print(t)
print(t.count(1))
print(t.index(2))

for i in t:
    print(i)

print("JAVA" in t)
print(t[6])
t[6].append(40)
print(t)
