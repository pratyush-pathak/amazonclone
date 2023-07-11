def is_prime(n):
    c=0
    for i in range(2,int(n/2+1)):
        if(n%i==0):
            c=1
            break
    if(n==1 or n==0):
        return False
    elif(c==0):
        return True
    else:
        return False

n = int(input("enter till where sum of prime no : "))
s=0
for i in range(1,n+1):
    if(is_prime(i)):
        s += i
    
print("Sum of Prime Numbers are : ", s)