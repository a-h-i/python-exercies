from exercises.linked_lists.linked_list import LinkedList


def remove_duplicates(linked_list: LinkedList):
    current = linked_list.head
    prev = None
    items = set()
    while current is not None:
        if current.data in items:
            prev.next = current.next
        else:
            items.add(current.data)
            prev = current
        current = current.next