age=int(input("Enter your age"))
gen=input("Enter your gender")
if(gen=='m'):
 if(age>=18):
    print("Valid for voting")
 if(age>=21):
    print("Valid for marriage")
else:
    print("Do you Study")
if(gen=='f'):
 if(age>=18):
    print("Valid for voting & marriage")
else:
    print("Do you Study")
