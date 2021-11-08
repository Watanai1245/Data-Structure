def greaterThan(index, array, x):
    if index > len(array) - 1:
        return 'No First Greater Value'

    if array[index] <= x:
        return greaterThan(index + 1, array, x)
    elif array[index] > x:
        return array[index]  

inlist, xlst = input('Enter Input : ').split('/')
inlist = [int(i) for i in inlist.split()]
xlst = [int(i) for i in xlst.split()]

inlist.sort()   

for i in xlst:
    print(greaterThan(0, inlist, i))