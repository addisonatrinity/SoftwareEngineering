/*************************************************************************
 *  Binary Search Tree class.
 *  Adapted from Sedgewick and Wayne.
 *
 *  @version 3.0 1/11/15 16:49:42
 *
 *  @author TODO
 *
 *************************************************************************/

import java.util.NoSuchElementException;

public class BST<Key extends Comparable<Key>, Value> {
	private Node root;             // root of BST

	private class Node {
		private Key key;           // sorted by key
		private Value val;         // associated data
		private Node left, right;  // left and right subtrees
		private int N;             // number of nodes in subtree

		public Node(Key key, Value val, int N) {
			this.key = key;
			this.val = val;
			this.N = N;
		}
	}

	
	public boolean isEmpty() { 
		return size() == 0; 
		}

	public int size() {
		return size(root); 
		}


	private int size(Node x) {
		if (x == null) return 0;
		else return x.N;
	}

	
	public boolean contains(Key key) {
		return get(key) != null;
	}

	
	public Value get(Key key) { return get(root, key); }

	private Value get(Node x, Key key) {
		if (x == null) return null;
		int cmp = key.compareTo(x.key);
		if      (cmp < 0) return get(x.left, key);
		else if (cmp > 0) return get(x.right, key);
		else              return x.val;
	}

	
	public void put(Key key, Value val) {
		if (val == null) { delete(key); return; }
		root = put(root, key, val);
	}

	private Node put(Node x, Key key, Value val) {
		if (x == null) return new Node(key, val, 1);
		int cmp = key.compareTo(x.key);
		if      (cmp < 0) x.left  = put(x.left,  key, val);
		else if (cmp > 0) x.right = put(x.right, key, val);
		else              x.val   = val;
		x.N = 1 + size(x.left) + size(x.right);
		return x;
	}

	public int height() {
		
		if(root == null) {
			return -1;
		} else if(size(root) == 1) {
			return 0;
		} else {
			return maxHeight(root);
		}

	}
	
	private int maxHeight(Node root) {

		if(root == null) {
			return -1;
		} else {
			int leftH = maxHeight(root.left);
			int rightH = maxHeight(root.right);

			if(leftH > rightH)
				return (leftH + 1);
			else 
				return (rightH + 1);
		}
	}

	
	public Key median() {

		if (isEmpty()) {
			return null;
		} else {
			return calcMedian(root, (root.N + 1)/2);
		}

	}

	private Key calcMedian(Node root, int N) {
		int count = size(root.left) +1;

		if(count == N) {
			return root.key;

		} else if(count > N) {
			return calcMedian(root.left, N);
		}
		return calcMedian(root.right, N - count);

	}


	public String printKeysInOrder() {
		if (isEmpty()) {
			return "()";
		} else {
			return calcKeysInOrder(root);
		}
	}


	private String calcKeysInOrder(Node root) {

		if(root == null) {
			return "()";

		} else {
			return("(" + calcKeysInOrder(root.left) + root.key + calcKeysInOrder(root.right) + ")");
		}
	}


	public String prettyPrintKeys() {
		return printingKeys(root, "");
	}


	private String printingKeys(Node root, String pre) {

		if(root == null) {
			return pre + "-null\n";
		}
		return (pre
				+ "-"
				+ root.key
				+ "\n"
				+ printingKeys(root.left, pre + " |")
				+ printingKeys(root.right, pre + "  "));

	}
	
	
	public void delete(Key key) {
		root = deleteNode(root, key);

	}

	private Node deleteNode(Node root, Key key) {
		if(root == null) {
			return null;
		}

		int cmp = key.compareTo(root.key);
		if(cmp > 0) {
			root.right = deleteNode(root.right, key);

		} else if(cmp < 0) {
			root.left = deleteNode(root.left, key);
			
		}else {
			if(root.left == null) {
				return root.right;
			}
			else if(root.right == null) {
				return root.left;
			}

			Node newNode = root;
			root = end(newNode.left);
			root.left = deletion(newNode.left);
			root.right = newNode.right;
		}

		root.N = size(root.left) + size(root.right) + 1;
		return root;

	}

	private Node deletion(Node root) {
		
		return deleteNode(root, end(root).key);

	}

	private Node end(Node root) {
		
		if(root.right == null) {
			return root;
		} else {
			return end(root.right);
		}
	}

}