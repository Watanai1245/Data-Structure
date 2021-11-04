class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = Node(node)
        else:
            root = self.root
            while True:
                if node < root.data:
                    if root.left is None:
                        root.left = Node(node)
                        break
                    root = root.left
                else:
                    if root.right is None:
                        root.right = Node(node)
                        break
                    root = root.right
        return self.root

def height(obj, level=0):
    if obj != None:
        l.append(level)
        height(obj.right, level + 1)
        height(obj.left, level + 1)
        return str(max(l))
    return str(max(l))

l = []
print(" *** Binary Search Tree Height ***")
tree = BinarySearchTree()
inp = list(map(int, input("Enter Input : ").split()))
for e in inp:
   tree.insert(e)
print("Height = ",height(tree.root),end="\n\n")
