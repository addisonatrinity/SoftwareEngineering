import networkx as nx           #find the shortest path between nodes in a directed graph
from Graph import Graph

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
 
 #          1
 #        /   \
 #       2     3
 #      / \   / \
 #     4   5  6   7

#imported a graph class from python libraries, created a graph with associaed vertices/edges.
G=nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 4), (2,5), (3, 4), (3, 5), (4, 5)])

#   
#       (1)_____
#      /   \    \
#   (2)    (3)    \
#   / \    /  \    |
#  / -->(4)    |   |
#  |      \    |  /
#   \_______ (5) /