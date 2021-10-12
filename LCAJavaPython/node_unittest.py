import node             #importing code from node
import unittest         #importing unit test


class TestLca(unittest.TestCase):

    def test_node1(self):
        self.assertEqual(node.findLCA(node.root, 4, 6).key, 1)

    def test_node2(self):
        self.assertEqual(node.findLCA(node.root, 4, 5).key, 2)

    def test_node3(self):
        self.assertEqual(node.findLCA(node.root, 3, 4).key, 1)

    def test_node4(self):
        self.assertEqual(node.findLCA(None, 4, 5), None)

    def test_node5(self):
        self.assertEqual(node.findLCA(node.root, 1, 5).key, 1)

    def test_node6(self):
        self.assertEqual(node.findLCA(node.root, 1, 1).key, 1)

    def test_node7(self):
        self.assertEqual(node.findLCA(node.root, 2, 3).key, 1)

    def test_node8(self):
        self.assertEqual(node.findLCA(node.root, 6, 7).key, 3)

    def test_node9(self):
        self.assertEqual(node.findLCA(node.root, 8, 8), None)


if __name__ == '__main__':
    unittest.main()