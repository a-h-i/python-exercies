from exercises.linked_lists.linked_list import LinkedList



def get_number_representation(linked_list: LinkedList) -> int:
    if linked_list.head is None:
        raise ValueError("List is empty")
    digit_index = 0
    number = 0
    current = linked_list.head
    while current is not None:
        number += current.data * 10 ** digit_index
        current = current.next
        digit_index += 1
    return number


def add_digits(list_a: LinkedList, list_b: LinkedList) -> int:
    a = get_number_representation(list_a)
    b = get_number_representation(list_b)
    return a + b