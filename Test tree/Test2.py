def Min(lst,i,min):
    value = int(lst[i])
    if(value <= min):
        min = value
    i += 1
    if(i < len(lst)):
        Min(lst,i,min)
    if(i == len(lst)):
        print("Min : " + str(min))

lst = [e for e in input("Enter Input : ").split(" ")]
Min(lst,0,+99999)