alphabat=[]
n=int(input("Enter value of size"))
for a in range(n):
    alphabat.append(input("Enter list of item"))
print(alphabat)
alphabat.sort(reverse=True)
print ("Ascending Order",sorted(alphabat))
print ("Descending Order",alphabat)
print()
