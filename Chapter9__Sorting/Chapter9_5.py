def bubbleSortLength(subList):
    for loop in range(1, len(subList)):
        swap = False

        for i in range(len(subList) - loop):
            if len(subList[i]) > len(subList[i + 1]):
                subList[i], subList[i + 1] = subList[i + 1], subList[i]
                swap = True

        if swap is False:
            break
    return subList


def bubbleSortNum(subList):
    for loop in range(1, len(subList)):
        swap = False

        for i in range(len(subList) - loop):
            if subList[i] > subList[i + 1]:
                subList[i], subList[i + 1] = subList[i + 1], subList[i]
                swap = True

        if swap is False:
            break
    return subList

def subListSum(ans, lst, index=0, result=None, carry=None):

    if result is None:
        result = []
    if carry is None:
        carry = []

    if index >= len(lst):  
        return result

    carry.append(lst[index])

    if sum(carry) == ans: 
        result.append(carry.copy())

    result = subListSum(ans, lst, index + 1, result, carry)
    carry.pop()
    result = subListSum(ans, lst, index + 1, result, carry)
    return result


ans, lst = input('Enter Input : ').split('/')
ans = int(ans)
lst = [int(i) for i in lst.split()]

subList = []

lst = bubbleSortNum(lst)
subList = subListSum(ans, lst)

if len(subList) != 0:
    for i in bubbleSortLength(subList):
        print(i)
else:
    print('No Subset')
