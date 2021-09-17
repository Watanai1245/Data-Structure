str1 , str2 = input(f"Enter Input : ").split("/")
list0 = str1.split(",")
list1 = str2.split(",")
list2 =[]

def group(inp):
    out=[]
    out[:0]=inp
    return int(out[0])

for i in range(len(list1)):
    chr = list1[i]
    if(chr != 'D'):
        en = chr.split(" ")
        same = False
        for j in range(len(list2)):
            if(group(str(en[1])) == group(str(list2[j]))):
                if(j+1 < len(list2)):
                    if(group(str(en[1])) != group(str(list2[j+1]))):
                        list2.insert(j+1,en[1])
                        same = True
                        break

        if(same == False):
            list2.append(en[1])
        
    if(chr == 'D'):
        if(list2 != []):
            print(list2.pop(0))
        else:
            print("Empty")
         
             
        