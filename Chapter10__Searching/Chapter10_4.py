class hash:
    def __init__(self, size, maxCol, thres):
        self.lst = [None] * size
        self.storeData = []
        self.maxCol = maxCol
        self.thres = thres
        self.tableSize = size
        self.realSize = 0

        print('Initial Table :')
        self.printTable()

    def printTable(self):
        for i in range(self.tableSize):
            print(f'#{i+1}\t{self.lst[i]}')
        print('----------------------------------------')

    def loadFactor(self):
        return self.realSize / self.tableSize * 100

    def insert(self, value):
        if value not in self.storeData:
            print(f'Add : {value}')
            self.storeData.append(value) 

        indexFirst = value % self.tableSize
        isMaxCol = False

        for n in range(maxCollision):
            index = (indexFirst + n**2) % self.tableSize 
            if self.lst[index] is not None:
                print(f'collision number {n+1} at {index}') 
            else:
                self.lst[index] = value  
                self.realSize += 1
                break
        else:
            isMaxCol = True                             

        if self.loadFactor() > self.thres:
            print('****** Data over threshold - Rehash !!! ******')
            self.rehash()
        elif isMaxCol is True:       
            print('****** Max collision - Rehash !!! ******')
            self.rehash()


    def rehash(self):
        self.tableSize = self.greaterPrimeNum()    
        self.lst = [None] * self.tableSize       
        self.realSize = 0                       

        for i in self.storeData: 
            self.insert(i)

    def greaterPrimeNum(self):
        newPrime = self.tableSize * 2 
        while True:
            isPrime = False
            for i in range(2, newPrime):  
                if newPrime % i == 0:
                    break
            else:
                isPrime = True           

            if isPrime is True:       
                break
            else:
                newPrime += 1        

        return newPrime         

print(' ***** Rehashing *****')
require, inputlst = input('Enter Input : ').split('/')

require = list(map(int, require.split()))
tableSize, maxCollision, threshold = require[0], require[1], require[2]
inputlst = list(map(int, inputlst.split()))
hashTable = hash(tableSize, maxCollision, threshold)
for i in inputlst:
    hashTable.insert(i)
    hashTable.printTable() 