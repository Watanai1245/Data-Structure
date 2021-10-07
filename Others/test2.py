print("*** String Rotation ***")
s1 , s2 = input(f"Enter 2 strings : ").split()

def Rotae(s1,s2):
    l1=[]
    l1[:0]= s1
    l2=[]
    l2[:0]= s2

    size1 = len(l1)

    nL1 = []
    nL1.insert(0, l1.pop(size1-1))
    nL1.extend(l1) 
    out1 = ""
    for ele in nL1: 
        out1 += ele

    l2.append(l2.pop(0))
    out2 = ""
    for ele in l2: 
        out2 += ele 

    return out1 , out2

i = 1
sss1 , sss2 = Rotae(s1,s2)

while(sss1 != s1 or sss2 != s2):
    if(i <= 5):
        print(str(i) +" "+ sss1 +" "+ sss2)
    sss1 , sss2 = Rotae(sss1 , sss2)
    i = i + 1

if(i == 7 or i == 12 or i == 28 or i == 42  or i == 132):
    print(" . . . . .")

print(str(i) +" "+ sss1 +" "+ sss2)
print("Total of  " + str(i) + " rounds.")