fruitlist=[]
n=int(input("Enter size of fruits"))
for a in range(n):
    fruitlist.append(input("Enter any fruit"))
print(fruitlist)
fruit=input("Enter fruit list")
if fruit in fruitlist:
    print("Found")
else:
    fruitlist.append(fruit)
print(fruitlist)
