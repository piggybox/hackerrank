"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    p1 = head  # slow pointer
    p2 = head  # faster pointer

    cycle = False

    while p1 != None and p2 != None and p2.next != None:
        p2 = p2.next.next
        p1 = p1.next

        if p1 == p2:
            cycle = True
            break

    return cycle