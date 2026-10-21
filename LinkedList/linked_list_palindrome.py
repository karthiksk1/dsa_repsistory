"""
Problem: Check Whether a Linked List Is a Palindrome

Description:
Check whether node values read the same forward and
backward. Restores the original list after checking.

Example:
Input:  [1, 2, 2, 1]
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


def list_values(head):
    result = []
    current = head
    while current is not None:
        result.append(current.data)
        current = current.next
    return result


def reverse_list(head):
    previous = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


def is_palindrome(head):
    if head is None or head.next is None:
        return True

    # Find end of first half
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second_half_head = reverse_list(slow.next)

    # Compare both halves
    result = True
    first = head
    second = second_half_head
    while second is not None:
        if first.data != second.data:
            result = False
            break
        first = first.next
        second = second.next

    # Restore original list
    slow.next = reverse_list(second_half_head)
    return result


head = create_list([1, 2, 2, 1])
print("Is palindrome:", is_palindrome(head))
