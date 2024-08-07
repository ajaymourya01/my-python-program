a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
c=int(input("Enter value of c"))
if a>b:
    if a>c:
        print("A is Greater than b & c")
    else:
        print("A and C are Equal")
elif b>c:
    if b>a:
        print("B is Greater than a & c")
    else:
        print("B and A are equal ")
elif c>a:
    if c>b:
        print("C is Greater than a & b")
    else:
        print("C and B are equal ")
else:
    print("They are equal")
