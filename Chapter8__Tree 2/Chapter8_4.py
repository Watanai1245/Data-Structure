PList, GList = input('Enter Input : ').split('/')
PList = [int(i) for i in PList.split()]
GList = [str(i) for i in GList.split(',')]

sumList = []


def recursionTree(n):
    sum = 0        

    if n >= len(PList):           
        return 0

    sum += recursionTree(2 * n + 1) 
    sum += recursionTree(2 * n + 2)    
    return PList[n] + sum       


print(recursionTree(0))          

for i in GList:
    i = list(map(int, i.split()))     
    sum1 = recursionTree(i[0])        
    sum2 = recursionTree(i[1])      

    if sum1 > sum2:
        print(i[0], '>', i[1], sep='')
    elif sum1 < sum2:
        print(i[0], '<', i[1], sep='')
    else:
        print(i[0], '=', i[1], sep='')