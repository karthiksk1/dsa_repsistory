"""
Problem: Detect a Cycle in a Linked List

Description:
Return True if a node's next pointer eventually leads
back to a previously visited node.

Example:
List: 1 -> 2 -> 3 -> 4
Node 4 points back to node 2.
Output: True
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_list(arr):
    head = None
    tail = None
    for value in arr:
        new_node = Node(value)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head


def has_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


head = create_list([1, 2, 3, 4])
# Create a cycle: node 4 points back to node 2
head.next.next.next.next = head.next
print("Contains cycle:", has_cycle(head))
