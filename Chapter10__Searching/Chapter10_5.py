def MWeight(lst, box):
    if box == 1:
        return sum(lst)

    minWeight = 99999
    for index in range(len(lst)):

        if len(lst[index:]) < box-1:
            break

        leftV = sum(lst[:index])
        rightV = MWeight(lst[index:], box - 1)

        minWeight = min(max(leftV, rightV), minWeight)

    return minWeight


weightlst, k = input('Enter Input : ').split('/')
k = int(k)
weightlst = [int(i) for i in weightlst.split()]

ans = MWeight(weightlst, k)
print(f'Minimum weigth for {k} box(es) = {ans}')