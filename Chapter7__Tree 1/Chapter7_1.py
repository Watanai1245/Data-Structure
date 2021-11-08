class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)  
        if self.root is None: 
            self.root = newNode
        else:
            CNode = self.root
            while True:
                if data > CNode.data:
                    if CNode.right is None:
                        CNode.right = newNode
                        break
                    CNode = CNode.right

                elif data < CNode.data: 
                    if CNode.left is None:  
                        CNode.left = newNode 
                        break
                    CNode = CNode.left 

        return self.root  

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level + 1)
        print('     ' * level, node.data)
        self.printTree(node.left, level + 1)


input = [int(i) for i in input('Enter Input : ').split()]

tree = BinarySearchTree()

for i in input:
    root = tree.insert(i)

tree.printTree(root)

