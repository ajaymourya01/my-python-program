num=int(input("Enter Any Number"))
count=0
i=0
fruitlist=[]
for a in range (num):
    fruitlist.append(input("Enter fruit name"))
print(fruitlist)
fruit=input("Enter your fruit")
for a in (fruitlist):
    count=count+1
if fruitlist==count:
    print("Found")
else:
    print("Not Found")
    fruitlist.append(fruit)
print(fruitlist)
