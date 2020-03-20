import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return

        if value < self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)
        # compare value to the current node
        # if smaller, go left
        # if bigger, go right

        # if no node to go to, (either left or right)
            # make the new node at that spot

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
       
        # --- recurse ---
        # compare value to the current node value
        # if smaller, go left
        # if bigger, go right
        # if equal, return True!
        # --- recurse ---
        
        # if smaller, but can't go left, return false
        # if larger, but can't go right, return false

    # Return the maximum value found in the tree
    def get_max(self):
        # get the value to the most right
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # left first
        if node.left is not None:
            node.left.in_order_print(node.left)

        print(node.value)

        # print right second
        if node.right is not None:
            node.right.in_order_print(node.right)
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue of nodes
        queue = Queue()
        # add current node to queue
        queue.enqueue(node)
        # while queue is not empty:
        while queue.len() > 0:
            # dequeue the node
            node = queue.dequeue()
            # print node
            print(node.value)
            # add its children
            # add left (if available)
            if node.left is not None:
                self.bft_print(node.left)
            # add right (if available) 
            if node.right is not None:
                self.bft_print(node.right)


        pass
        #      6
        #    /   \
        #   3     5
        #  / \   / \
        # 1   2 4   7

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        #      3
        #     / \
        #    /   \
        #   2     5
        #  /     /
        # 1     4
        # create a node_stack
        # node_stack = 
        # push the left value of the current node on

        # while we have items on stack

            # push the left value of current node if we can

            # print the current value


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(6)

bst.insert(3)
bst.insert(1)
bst.insert(2)
bst.insert(5)
bst.insert(4)
bst.insert(7)

bst.bft_print(bst)