A = int(input("Enter Input : "))
size = 4 + 2*A
for i in range(size//2,0,-1):
    for j in range(1,size+1,1):
        if(j<i and j<=(size//2)):
            print(".",end="")
        elif(j<=(size//2)):
            print("#",end="")
        elif(j>=(size//2) and (i==size//2 or i==1 or j==(size//2)+1 or j==size)):
            print("+",end="")
        else:
            print("#",end="")
    print("")
for i in range (1,(size//2)+1,1):
    for j in range(1,size+1,1):
        if(j<=size//2):
            if((i==1 or i==size//2 or j==1 or j==size//2)):
                print("#",end="")
            else:
                print("+",end="")
        if(j> size//2):
            if((j-(size//2))+i-1 > (size//2)):
                print(".",end="")
            else:
                print("+",end="")
    print("")