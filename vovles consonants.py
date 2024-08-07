char=str(input("Enter Any Characters"))
if char>='a' or char<='z' and char >='A' and char<='Z':
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        print("Vovals",char)
    else:
        print("Consonants",char)

else:
    print("Wrong value")
 
