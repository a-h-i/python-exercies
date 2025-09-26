import pytest

from exercises.linked_lists.linked_list import LinkedList
from exercises.linked_lists.add_digits import add_digits

@pytest.fixture()
def list_a():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(0)
    linked_list.append(3)
    return linked_list


@pytest.fixture()
def list_b():
    linked_list = LinkedList()
    linked_list.append(0)
    linked_list.append(1)
    linked_list.append(1)
    return linked_list


def test_add_digits(list_a: LinkedList, list_b: LinkedList):
    assert add_digits(list_a, list_b) == 411
