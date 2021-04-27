class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def levelOrder(root):
    hash = {}  # to keep node info on every level

    def traversal(node, level):
        if node != None:
            if level in hash:
                hash[level].append(node.info)
            else:
                hash[level] = [node.info]

            level1 = traversal(node.left, level + 1)
            level2 = traversal(node.right, level + 1)
            return max(level1, level2)
        else:
            return level

    max_level = traversal(root, 0)

    # convert hash to list
    result = []
    for k in range(max_level):
        for item in hash[k]:
            print(item, end=" ")
