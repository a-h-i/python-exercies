from exercises.linked_lists.linked_list import LinkedList, ListNode


def partition_list(linked_list: LinkedList, pivot):
    less_than_list = LinkedList()
    greater_or_equal_to_list = LinkedList()
    current_node = linked_list.head
    while current_node is not None:
        if current_node.data < pivot:
            less_than_list.append(current_node.data)
        else:
            greater_or_equal_to_list.append(current_node.data)
        current_node = current_node.next

    linked_list.head = less_than_list.head
    current_node = less_than_list.head
    while current_node.next is not None:
        current_node = current_node.next
    current_node.next = greater_or_equal_to_list.head

