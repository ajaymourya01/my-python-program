num=int(input("Enter any number"))
temp=num
sum=0
cube=0
r=0
count=0
while num>0:
    r=num%10
    count=1
    cube=(r**count)
    sum=cube
    num=int(num/10)
if sum==temp:
    print("Armstrong")
else:
    print("Not a Armstrong") 
