class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f'({self.key}, {self.value})'


class hash:
    def __init__(self, size, maxCol):
        self.lst = [None] * size    
        self.maxCol = maxCol          
        self.tableSize = size      
        self.realSize = 0           

    def printTable(self):
        for i in range(self.tableSize):         
            print(f'#{i+1}\t{self.lst[i]}')
        print('---------------------------')

    def insert(self, key, value):
        if self.realSize == self.tableSize:
            return False                   

        newData = Data(key, value)          
        sum = 0
        for i in key:
            sum += ord(i)
        indexFirst = sum % self.tableSize   

        for n in range(self.maxCol):
            index = (indexFirst + n**2) % self.tableSize       

            if self.lst[index] is not None:
                print(f'collision number {n+1} at {index}')     
            else:
                self.lst[index] = newData         
                self.realSize += 1            
                break                          
        else:
            print('Max of collisionChain')      

        return True    

print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')
tableSize, maxColis = map(int, inp[0].split())
lst = inp[1].split(',')

hashTable = hash(tableSize, maxColis)

for i in lst:
    i = i.split()
    canInsert = hashTable.insert(i[0], i[1])   

    if canInsert is True: 
        hashTable.printTable()
    else:
        print('This table is full !!!!!!')  
        break