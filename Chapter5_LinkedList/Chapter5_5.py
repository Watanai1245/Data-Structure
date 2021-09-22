class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None, None)

    def __str__(self):
        s = ''
        p = self.head.next
        while p is not None:
            s += str(p.data)
            if p.next is not None:
                s += ' -> '
            p = p.next
        return s

    def display(self):
        s = ''
        p = self.head.next
        while p is not None:
            s += str(p.data) + ' '
            p = p.next
        return s

    def size(self):
        count = 0
        p = self.head.next
        while p is not None:
            count += 1
            p = p.next
        return count

    def checkMaxAndInsert(self, newValue):
        p = self.head.next
        for index in range(self.size()):
            if newValue > p.data:
                self.insert(index, newValue)
                return
            p = p.next
        else:
            self.append(newValue)

    def isEmpty(self):
        return self.size() == 0

    def nodeAt(self, index):
        p = self.head
        for _ in range(-1, index):
            p = p.next
        return p

    def insert(self, index, data):
        prevNode = self.nodeAt(index - 1)
        newNode = Node(data, prevNode.next)
        prevNode.next = newNode

    def append(self, data):
        self.insert(self.size(), data)

    def pop(self, index):
        if self.isEmpty():
            return 'No more to pop'
        if index > self.size() - 1:
            return 'out of range'

        prevNode = self.nodeAt(index - 1)
        nextNode = prevNode.next.next
        popNode = prevNode.next
        prevNode.next = nextNode
        return popNode

def radixSort(linkedList):
    state = False
    time = 0
    size = linkedList.size()
    zeroL = SinglyLinkedList()
    oneL = SinglyLinkedList()
    twoL = SinglyLinkedList()
    threeL = SinglyLinkedList()
    fourL = SinglyLinkedList()
    fiveL = SinglyLinkedList()
    sixL = SinglyLinkedList()
    sevenL = SinglyLinkedList()
    eightL = SinglyLinkedList()
    nightL = SinglyLinkedList()

    for digit in range(1000):
        for _ in range(size):
            popNode = linkedList.pop(0)

            originalData = popNode.data
            if originalData >= 0:
                calculatedData = originalData // 10 ** digit
            else:
                calculatedData = -originalData // 10 ** digit

            if calculatedData % 10 == 0:
                zeroL.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 1:
                oneL.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 2:
                twoL.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 3:
                threeL.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 4:
                fourL.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 5:
                fiveL.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 6:
                sixL.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 7:
                sevenL.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 8:
                eightL.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 9:
                nightL.checkMaxAndInsert(originalData)

        print('------------------------------------------------------------')
        print('Round :', digit + 1)
        print('0 :', zeroL.display())
        print('1 :', oneL.display())
        print('2 :', twoL.display())
        print('3 :', threeL.display())
        print('4 :', fourL.display())
        print('5 :', fiveL.display())
        print('6 :', sixL.display())
        print('7 :', sevenL.display())
        print('8 :', eightL.display())
        print('9 :', nightL.display())

        if not zeroL.isEmpty() and oneL.isEmpty() and twoL.isEmpty() and \
                threeL.isEmpty() and fourL.isEmpty() and fiveL.isEmpty() and \
                sixL.isEmpty() and sevenL.isEmpty() and eightL.isEmpty() and nightL.isEmpty():
            state = True

        while not zeroL.isEmpty(): linkedList.append(zeroL.pop(0).data)
        while not oneL.isEmpty(): linkedList.append(oneL.pop(0).data)
        while not twoL.isEmpty(): linkedList.append(twoL.pop(0).data)
        while not threeL.isEmpty(): linkedList.append(threeL.pop(0).data)
        while not fourL.isEmpty(): linkedList.append(fourL.pop(0).data)
        while not fiveL.isEmpty(): linkedList.append(fiveL.pop(0).data)
        while not sixL.isEmpty(): linkedList.append(sixL.pop(0).data)
        while not sevenL.isEmpty(): linkedList.append(sevenL.pop(0).data)
        while not eightL.isEmpty(): linkedList.append(eightL.pop(0).data)
        while not nightL.isEmpty(): linkedList.append(nightL.pop(0).data)

        if state is True:
            break
        time += 1
    return linkedList, time

inp = [int(i) for i in input('Enter Input : ').split()]

L = SinglyLinkedList()
L_Origin = SinglyLinkedList()

for i in inp:
    L.append(i)
    L_Origin.append(i)

time = 0
radixLinked, time = radixSort(L)
print('------------------------------------------------------------')
print(time, 'Time(s)')
print('Before Radix Sort :', L_Origin)
print('After  Radix Sort :', radixLinked)