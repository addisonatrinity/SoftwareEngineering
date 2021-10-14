import node             #importing code from node
import unittest         #importing unit test



class TestLca(unittest.TestCase):
#           1
 #        /   \
 #       2     3
 #      / \   / \
 #     4   5  6   7

    def test_node1(self):
        test1 = node.findLCA(node.root, 4, 6).key
        self.assertEqual(test1, 1)

    def test_node2(self):
        test2 = node.findLCA(node.root, 4, 5).key
        self.assertEqual(test2, 2)

    def test_node3(self):
        test3 = node.findLCA(node.root, 3, 4).key
        self.assertEqual(test3, 1)

    def test_node4(self):
        test4 = node.findLCA(None, 4, 5)
        self.assertEqual(test4, None)

    def test_node5(self):
        test5 = node.findLCA(node.root, 1, 5).key
        self.assertEqual(test5, 1)

    def test_node6(self):
        test6 = node.findLCA(node.root, 1, 1).key
        self.assertEqual(test6, 1)

    def test_node7(self):
        test7 = node.findLCA(node.root, 2, 3).key
        self.assertEqual(test7, 1)

    def test_node8(self):
        test8 = node.findLCA(node.root, 6, 7).key
        self.assertEqual(test8, 3)

    def test_node9(self):
        test9 = node.findLCA(node.root, 8, 8)
        self.assertEqual(test9, None)

    def test_emptyTree(self):                             
        test10 = node.findLCA(None, None, None)
        self.assertEqual(test10, None)

if __name__ == '__main__':
    unittest.main()