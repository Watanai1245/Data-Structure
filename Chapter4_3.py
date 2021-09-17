str = input(f"Enter Input : ").split("/")
list1 = str[0].split(" ")
list2 = str[1].split(",")

for i in range(len(list2)):
    chr = list2[i]
    if(chr != 'D'):
        en = chr.split(" ")
        list1.append(en[1])
    if(chr == 'D'):
        list1.pop(0)

list3 = list(dict.fromkeys(list1))
if(list1 == list3):
    print("NO Duplicate")
else:
    print("Duplicate")


