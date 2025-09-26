import pytest

from exercises.linked_lists.is_palindrome import is_palindrome
from exercises.linked_lists.linked_list import LinkedList


@pytest.fixture
def palindrome_odd():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(1)
    return linked_list

@pytest.fixture
def palindrome_even():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(2)
    linked_list.append(1)
    return linked_list

@pytest.fixture
def not_palindrome_odd():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    return linked_list

@pytest.fixture
def not_palindrome_even():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    return linked_list

@pytest.fixture
def empty_list():
    return LinkedList()

def test_palindrome(palindrome_odd, palindrome_even, not_palindrome_odd, not_palindrome_even, empty_list):
    assert is_palindrome(palindrome_odd)
    assert is_palindrome(palindrome_even)
    assert not is_palindrome(not_palindrome_odd)
    assert not is_palindrome(not_palindrome_even)
    assert is_palindrome(empty_list)