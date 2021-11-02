from collections import Counter


class LinkedList:
    def __init__(self, list=None):
        if list == None:
            self.word = []
        else:
            self.word = list

    def push(self, i):
        self.word.append(i)

    def pop(self):
        return self.word.pop()

    def isEmpty(self):
        return self.word == []

    def size(self):
        return len(self.word)

    def reverse(self):
        newList = []
        for i in range(len(self.word)):
            newList.append(self.word.pop())
        self.word.extend(newList)

    def extend(self, list):
        self.word.extend(list)

    def __str__(self):
        if not self.isEmpty():
            out = "Linked data : "
            for word in self.word:
                out += str(word)+' '
            return out
        return 'Empty'

    def sort(self):
        newList = []
        while self.word:
            minimum = self.word[0]
            for x in self.word:
                if x < minimum:
                    minimum = x
            newList.append(minimum)
            self.word.remove(minimum)
        self.word = newList


def findMean(lst):
    sum = 0
    for i in lst:
        sum = sum+int(i)
    Mid = float(sum/len(lst))
    print("Mean = %.2f" % Mid)


def findmedian(lst):
    for i in range(0, len(lst)):
        lst[i] = int(lst[i])

        

    if((len(lst) %2) != 0):
        q = int((len(lst)+1)/2)
        print(q)
        print(lst)
        medium = lst[q-1]
        print("Median =",medium)
    else:
        x1 = int((len(lst))/2)
        x2 = int(((len(lst))/2)+1)
        x = lst[x1]
        y = lst[x2]
        medium = (x+y) / 2
        print("Median =",medium)



inputlists = [int(e) for e in input('Enter numbers : ').split()]
lst = LinkedList()
lst.extend(inputlists)
print("Output :")
lst.sort()
print(lst)
print("Amount of data =", lst.size())
lst = [e for e in str(lst).split(' ')]
findMean(inputlists)
findmedian(inputlists)
#print(findmedian(lst).replace("'", ""))