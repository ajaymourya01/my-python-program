n=int(input("Enter vlaue of list"))
itemlist=[]
for a in range (n):
    itemlist.append(input("Enter your item"))
print(itemlist)
item=input("Enter item")
if item in itemlist:
    itemlist.remove(item)
else:
    print("Not found")
print(itemlist)
