import sys
class Queue :
    def __init__(self,list = None) :
        self.items = []
        self.word = []

    
    def enQueue(self,i):
        self.items.append(i)
        
    def deQueue(self):
        return self.word.pop(0)
    
    def isEmpty(self):
        return self.word == []

    def size(self):
        return len(self.word)

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1
         

q = Queue()
input = (e for e in (input("Enter Input : ").split(",")))
for e in input:
    q.enQueue(e)
s = []
for i in range(0,len(q.items)) :
    s = q.items[i].split()
    if (s[0] == 'E'):
        q.word.append(s[1:len(s)])
        print(q.size())
    if (s[0] == 'D'):
        if(q.size() == 0) :
            print('-1')
        else:
            print(listToString(q.deQueue()),'0')

if(q.size() == 0) :
    print("Empty")
else :
    d = []
    for i in range(0,len(q.word)):
        d.append(listToString(q.word[i]))
    for j in range(0,len(d)):
        a = d.pop(0)
        sys.stdout.write(str(a))
        sys.stdout.write(" ")
        
