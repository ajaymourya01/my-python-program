num=int(input("Enter any number"))
rem=0
temp=num
sum=0
while num>0:
    rem=num%10
    sum=(sum*10)+rem
    num=int(num/10)
if sum==temp:
    print("Palindrome ")
else:
    print("Not a Palindrome")  
