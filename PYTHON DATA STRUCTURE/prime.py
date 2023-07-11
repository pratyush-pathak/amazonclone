n = int(input("Enter a number "))
f=0
for i in range(2,int(n/2+1)):
  if(  n % i == 0):
    f=1
    break
  
if(n==0):
    print("Number entered id 0")
elif(n==1):
    print(n, "is not a Prime Number")
elif(f==0):
    print(n, "is a Prime Number")
else:
    print(n, "is not a Prime Number")
     