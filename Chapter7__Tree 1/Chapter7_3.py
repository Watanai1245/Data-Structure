class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                

def father(r,data):
	if r.data == data:
		return f'None Because {data} is Root'

	cur_node = r
	while cur_node.right != None or cur_node.left != None:
		if cur_node.right != None and cur_node.right.data == data:
			return cur_node.data
		elif cur_node.left != None and cur_node.left.data == data:
			return cur_node.data
		elif data > cur_node.data:
			cur_node = cur_node.right
		elif data < cur_node.data:
			cur_node = cur_node.left
	return 'Not Found Data'

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
print(father(tree.root,data[1]))