
class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
     
def findLCA(root, n1, n2):
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)
 
    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca
 
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
print(findLCA(root, 4, 5).key)
print(findLCA(root, 4, 6).key)
print(findLCA(root, 3, 4).key)
print(findLCA(root, 2, 4).key)
 