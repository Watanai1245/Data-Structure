def bi_search(index, lastIndex, array, x):
    if index > lastIndex:
        return False

    mid = (index+lastIndex)//2 

    if x == array[mid]:
        return True
    elif x < array[mid]:
        return bi_search(index, mid-1, array, x)  
    elif x > array[mid]:                   
        return bi_search(mid+1, lastIndex, array, x)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))