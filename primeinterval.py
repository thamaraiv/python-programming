    a=input("Enter the first interval")
    b=input("enter the second interval")
    if(a>0):
        for num in range(a,b):
            a=a+1
            for i in range(2,3):
                if num%i==0:
                    break
                else:
                    print num," is a primenumber"
    else:
        print"positive input only"
