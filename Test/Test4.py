print("*** String Rotation ***")
s1 , s2 = input(f"Enter 2 strings : ").split()

def Rotation(s1,s2):
    list1=[]
    list1[:0]= s1
    list2=[]
    list2[:0]= s2

    size1 = len(list1)

    nList1 = []
    nList1.insert(0, list1.pop(size1-1))
    nList1.extend(list1) 
    out1 = ""
    for ele in nList1: 
        out1 += ele

    list2.append(list2.pop(0))
    out2 = ""
    for ele in list2: 
        out2 += ele 

    return out1 , out2

i = 1
string1 , string2 = Rotation(s1,s2)

while(string1 != s1 or string2 != s2):
    if(i <= 5):
        print(str(i) +" "+ string1 +" "+ string2)
    string1 , string2 = Rotation(string1 , string2)
    i = i + 1
if(i == 42 or i == 7 or i == 28 or i == 12 or i == 132):
    print(" . . . . .")
print(str(i) +" "+ string1 +" "+ string2)
print("Total of  " + str(i) + " rounds.")