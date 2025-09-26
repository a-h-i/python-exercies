import pytest

from exercises.linked_lists.linked_list import LinkedList
from exercises.linked_lists.remove_duplicates import remove_duplicates


@pytest.fixture
def test_list():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(1)
    linked_list.append(4)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    return linked_list


def test_remove_duplicates(test_list: LinkedList):
    remove_duplicates(test_list)
    assert test_list.head.data == 1
    assert test_list.head.next.data == 2
    assert test_list.head.next.next.data == 3
    assert test_list.head.next.next.next.data == 4
    assert test_list.head.next.next.next.next.data == 5
    assert test_list.head.next.next.next.next.next is None