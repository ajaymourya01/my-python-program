num=int(input("Enter any number"))
i=2
while i<=num:
    count=0
    j=2
    while j<=i:
         if i%j==0:
            count=count+1
            j=j+1
    if count==1:            
            print(i)
    i=i+1
