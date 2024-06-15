def printLine():
    print("*"*50)

printLine()    
print("This is user defined function in python")
printLine()    


def add(a,b):
    print("Addition : ", a+b)
printLine()    
add(10,20)
printLine()    

def sub(a,b):
    return a-b

printLine()    
print("Sub = ",sub(20,10))
printLine()    

ans=sub(30,15)
print("Sub = ",ans)
