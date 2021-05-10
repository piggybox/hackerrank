""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import math

# medium 

def checkBST(root):
    # top down approach
    def check(node, min, max):
        if node is None:
            return True
        if node.data <= min or node.data >= max:
            return False
        return check(node.left, min, node.data) and check(
            node.right, node.data, max)

    return check(root, -1 * math.inf, math.inf)
