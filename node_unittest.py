import node             #importing code from node
import unittest         #importing unit test
from Graph import Graph



class TestLca(unittest.TestCase):
#           1
 #        /   \
 #       2     3
 #      / \   / \
 #     4   5  6   7

    def test_emptyTree(self):                           #null test                          
        test10 = node.findLCA(None, None, None)
        self.assertEqual(test10, None)

    def test1(self):                                    #test n1->1, n2->1, LCA:1
        test1 = node.findLCA(node.root, 1, 1).key      
        self.assertEqual(test1, 1)

    def test2(self):                                    #test n1->4, n2->5, LCA:2
        test2 = node.findLCA(node.root, 4, 5).key       
        self.assertEqual(test2, 2)

    def test3(self):                                    #test n1->3, n2->4, LCA:1
        test3 = node.findLCA(node.root, 3, 4).key
        self.assertEqual(test3, 1)

    def test4(self):                                    #test n1->4, n2->5, LCA:None as no root
        test4 = node.findLCA(None, 4, 5)
        self.assertEqual(test4, None)

    def test5(self):                                    #test n1->1, n2->5, LCA:1
        test5 = node.findLCA(node.root, 1, 5).key
        self.assertEqual(test5, 1)                  

    def test6(self):                                    #test n1->4, n2->6, LCA:1
        test6 = node.findLCA(node.root, 4, 6).key
        self.assertEqual(test6, 1)

    def test7(self):                                    #test n1->2, n2->3, LCA:1
        test7 = node.findLCA(node.root, 2, 3).key
        self.assertEqual(test7, 1)

    def test8(self):
        test8 = node.findLCA(node.root, 6, 7).key       #test n1->6, n2->7, LCA:1
        self.assertEqual(test8, 3)

    def test9(self):
        test9 = node.findLCA(node.root, 9, 8)           #test, both numbers not in the tree, result null
        self.assertEqual(test9, None)

    def test_DAG(self):
        dagtest1 = node.findLCA(Graph, 2,3)
        self.assertEqual(dagtest1, 1)

        dagtest2 = node.findLCA(Graph,2,5)
        self.assertEqual(dagtest2, 2)

        dagtest3 = node.findLCA(Graph,1,4)
        self.assertEqual(dagtest3, 1)

if __name__ == '__main__':
    unittest.main()