def simpleinterest_fun(p,r,t):
    si=p*r*t/100
    print("Simple Interest=",si)
    print("Total Return of Amount=",p+si)
simpleinterest_fun(p=int(input("enter your amount=")),
                   r=int(input("enter your interest rate=")),
                   t=int(input("enter your period of time="))
                   )
