num=int(input("Enter any number"))
rev=0
a=int(num/100)%10
b=int(num/10)%10
c=int(num/1)%10
rev=c*100+b*10+a
if num==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
