from exercises.linked_lists.linked_list import LinkedList


def is_palindrome(linked_list: LinkedList) -> bool:
    stack = list()
    slow = linked_list.head
    fast = linked_list.head
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    if fast is not None:
        # has an odd number of elements, ignore the middle element
        slow = slow.next
    while slow:
        if slow.data != stack.pop():
            return False
        slow = slow.next
    return True