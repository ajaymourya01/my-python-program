num=int(input("Enter any number"))
rev=0
a=int(num/100000)%10
b=int(num/10000)%10
c=int(num/1000)%10
d=int(num/100)%10
e=int(num/10)%10
f=int(num/1)%10
rev=f*100000+e*10000+d*1000+c*100+b*10+a
if num==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
