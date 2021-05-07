class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(current):
    if current:
        print(current.data)
        preOrder(current.left)
        preOrder(current.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preOrder(root)