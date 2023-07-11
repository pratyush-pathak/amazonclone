n = int(input("enter the lenth of series "))
a= int(input("first digit ")) #0
b= int(input("second digit ")) #1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c
