class node :
    def __init__(self, data, next = None) :
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
            
    def __init__(self):                
            self.head = None
            self.size = 0
       
    def __str__(self) :
        return str(self.data)
    
class list :
    def __init__(self):  
        self.head = None

    def __init__(self):  
        self.head = self.tail = None

    def __init__(self, head = None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            t = t.next
            self.size += 1
            self.tail = 1
            
         

