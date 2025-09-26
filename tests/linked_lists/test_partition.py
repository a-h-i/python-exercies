import pytest

from exercises.linked_lists.linked_list import LinkedList
from exercises.linked_lists.partition_list import partition_list


@pytest.fixture()
def linked_list():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(2)
    linked_list.append(9)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(1)
    linked_list.append(2)
    return linked_list


def test_partition(linked_list):
    partition_list(linked_list, 4)
    as_list = linked_list.to_list()
    assert as_list == [1, 2, 2, 3, 1, 2, 9, 4, 4, 5, 6]