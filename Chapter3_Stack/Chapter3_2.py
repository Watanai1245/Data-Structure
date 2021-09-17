class Stack():
    def __init__(self,list = None):
        if list == None:
            self.word = []
        else:
            self.word = list
        
    def push(self,i):
        self.word.append(i)

    def pop(self):
        return self.word.pop()

    def isEmpty(self):
        return self.word == []

    def size(self):
        return len(self.word)

def parenMatching(str):
    s = Stack()
    i = 0
    error = 0
    c = str
    while i < len(str) and error == 0 :
        c = str[i] 
        if c in '{[(':
            s.push(c)
        else:
            if c in '}])':
                if s.size() > 0:
                    if not match(s.pop(),c):
                        error = 1
                else:
                    error = 2
        
        i += 1

    if c[-1] not in '}])':
        error = 3

    return error,c,i,s

def match(op,cl):
    opens = "([{"
    closes = ")]}"
    return opens.index(op) == closes.index(cl) 
    
str = input('Enter expresion : ')
err,c,i,s = parenMatching(str)
if err == 1:
    print(str , 'Unmatch open-close  ')
elif err == 2:
    print(str , 'close paren excess')
elif err == 3:
    print(str , 'open paren excess  ', s.size(), ': ',end=''  ) 
    for ele in s.word:
        print(ele,sep=' ',end = '')
    print()
else: 
    print(str, 'MATCH')