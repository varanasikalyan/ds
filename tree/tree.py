class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


n7 = Node(7, None, None)
n8 = Node(8, None, None)

n3 = Node(3, n7, n8)
n4 = Node(4, None, None)
n5 = Node(5, None, None)
n6 = Node(6, None, None)

n2 = Node(2, n5, n6)
n1 = Node(1, n3, n4)

n0 = Node(0, n1, n2)

def sum(root):
    if root == None:
        return 0
    return root.data + sum(root.left) + sum(root.right)

print(sum(n0))