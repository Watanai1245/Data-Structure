def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
inp=input("Enter Input : ").split()
a=int(inp[0])
b=int(inp[1])
if a==0 and b==0:
    print("Error! must be not all zero.")
elif a>0 and b>0:
    if a>b:
        print("The gcd of {} and {} is : {}".format(a,b,abs(gcd(a,b))))    
    else:
        print("The gcd of {} and {} is : {}".format(b,a,abs(gcd(b,a))))
elif a == 0 or b == 0:
    if a<b:
        print("The gcd of {} and {} is : {}".format(b,a,abs(gcd(b,a))))
    else:
        print("The gcd of {} and {} is : {}".format(a,b,abs(gcd(a,b))))
elif a<0 or b<0:
    if abs(a)<abs(b):
        print("The gcd of {} and {} is : {}".format(b,a,abs(gcd(b,a))))
    else:
        print("The gcd of {} and {} is : {}".format(a,b,abs(gcd(a,b))))