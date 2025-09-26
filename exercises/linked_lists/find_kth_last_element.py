from exercises.linked_lists.linked_list import LinkedList


def find_kth_last_element(linked_list: LinkedList, k: int):
    current = linked_list.head
    kth_last_element = None
    count = 1
    while current is not None:
        current = current.next
        if kth_last_element is not None:
            kth_last_element = kth_last_element.next
        if count == k:
            if kth_last_element is None:
                kth_last_element = linked_list.head
        count += 1
    return kth_last_element