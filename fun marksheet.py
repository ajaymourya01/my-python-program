def personalinfo_fun(stu, cls, roll):
    print("Student Name:",stu)
    print("Class:",cls)
    print("Roll No.:",roll)
personalinfo_fun("Ajay","12th",24523453)   
#personalinfo_fun(stu=str(input("enter student name")),
 #               roll=int(input("enter student roll")))
def sub_fun(hi,eng,che, phy,bio):
    print("Hindi marks:",hi)
    print("English marks:",eng)
    print("Chemistry marks:",che)
    print("Physics marks:",phy)
    print("Biology marks:",bio)
    total=hi+eng+che+phy+bio
    print("Total marks:",total)
    return total
    return hi,eng,che,phy,bio


t=sub_fun(hi=int(input("enter hindi marks")),
       eng=int(input("enter english marks")),
       che=int(input("enter chemistry marks")),
        phy=int(input("enter physics marks")),
        bio=int(input("enter biology marks")))

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

    
def carry_fun():
    count=0
    sub_fun(carry)
    if 33<=hi:
        count=count+1
        print("Carry in Hindi")
    if 33<=eng:
        count=count+1
        print("Carry in English")
    if 33<=che:
        count=count+1
        print("Carry in Chemistry")
    if 33<=phy:
        count=count+1
        print("Carry in Physics")
    if 33<=bio:
        count=count+1
        print("Carry in Biology")
    if count==2 or count==1:
        print("Supplimantry above subject")
    elif count>2:
        print("Supplimantry more than two subject")
    else:
        print("Pass")
carry_fun()
print(sub_fun)
