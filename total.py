def sub_fun(hi,eng,che, phy,bio):
    print("Hindi marks:",hi)
    print("English marks:",eng)
    print("Chemistry marks:",che)
    print("Physics marks:",phy)
    print("Biology marks:",bio)
    total=hi+eng+che+phy+bio
    print("Total marks:",total)
    return total
t=sub_fun(33,36,37,48,33)

def grade_fun():
    per=t/5
    if per>=75:
        print("Execellent A+")
    elif per>=60:
        print("Very Good A")
    elif per>=45:
        print("Good B")
    elif per>=33:
        print("Bad C")
    else:
        print("Fail")
grade_fun()
    
