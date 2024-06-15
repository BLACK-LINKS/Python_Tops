def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%1==0:
                print(n," Is not prime")
                break
            else:
                print(n." Is prime")
     else:
         print(n, " is not prime")


prime(23)         
