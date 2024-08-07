name=str(input("Enter your name"))
father=str(input("Enter your father name"))
mother=str(input("Enter your mother name"))
roll=int(input("Enter your roll number"))
app=int(input("Enter your app number"))
hi=int(input("Enter marks of Hindi"))
eng=int(input("Enter marks of Englidh"))
che=int(input("Enter marks of Chemistry"))
phy=int(input("Enter marks of Physics"))
bio=int(input("Enter marks of Biology"))
print("----------------------------------------")
print("Student Name",name)
print("Father Name",father)
print("Mother Name",mother)
print("Roll No.",roll)
print("Application No.",app)
total=hi+eng+che+phy+bio
print("----------------------------------------")
if hi>=75:
    print("Hindi in Distt**",hi)
if eng>=75:
    print("English in Distt**",eng)
if che>=75:
    print("Chemistry in Distt**",che)
if phy>=75:
    print("Physics in Distt**",phy)
if bio>=75:
    print("Biology in Distt**",bio)
print("total number ",total)
per=total/5
print("Percentage",per)
if per>75:
    print("A+",per)
elif per>60:
    print("A",per)
elif per>45:
    print("B",per)
elif per>33:
    print("C",per)
else:
    print("Fail")
c=0
if hi<33:
    c=c+1
    print("Carry in Hindi")
if eng<33:
    c=c+1
    print("Carry in English")
if che<33:
    c=c+1
    print("Carry in Chemistry")
if phy<33:
    c=c+1
    print("Carry in Physics")
if bio<33:
    c=c+1
    print("Carry in Biology")
if c==2 or c==1:
    print("Supplimantry above subject")
elif c>2:
    print("Supplimantary more than two subject")
else:
    print("Pass")
    
