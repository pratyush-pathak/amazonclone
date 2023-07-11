n = input("enter to check palindrome : ")

i = n[::-1]
if(n.upper()==i.upper()):
    print("Palindrome")
else:
    print("NOT palindrome")