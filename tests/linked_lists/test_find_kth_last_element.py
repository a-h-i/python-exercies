import pytest

from exercises.linked_lists.find_kth_last_element import find_kth_last_element
from exercises.linked_lists.linked_list import LinkedList


@pytest.fixture
def test_list():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)
    return linked_list


def test_find_kth_last_element(test_list: LinkedList,):
    assert find_kth_last_element(test_list, 1).data == 6
    assert find_kth_last_element(test_list, 2).data == 5
    assert find_kth_last_element(test_list, 3).data == 4
    assert find_kth_last_element(test_list, 4).data == 3
    assert find_kth_last_element(test_list, 5).data == 2
    assert find_kth_last_element(test_list, 6).data == 1