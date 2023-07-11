def sumofeven(a):
    b=sum(range(2,a+1,2))
    return b

n = int(input("enter a num till where sum of even needed"))
print(sumofeven(n))