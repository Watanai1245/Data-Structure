class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            root = Node(data)
            self.root = root
            return
        current = self.root

        while True:
            if data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    break
                else:
                    current = current.right
            elif data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    break
                else:
                    current = current.left
            else:
                break
        
        return self.root
    
    def checkpos(self, data):
        if self.root is None:
            print("Not exist")
            return
        if self.root.data == data:
            print("Root")
            return

        C = self.root
        while C is not None:
            if data == C.data:
                if C.left is None and C.right is None:
                    print("Leaf")
                else:
                    print("Inner")
                return
            elif data > C.data:
                C = C.right
            else:
                C = C.left 
        
        print("Not exist")

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])
    