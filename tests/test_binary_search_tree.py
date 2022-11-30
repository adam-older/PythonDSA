import pytest
from lib.binary_search_tree import BinarySearchTree

class TestBinarySearchTree:
    def test_test_method(self):
        bst = BinarySearchTree()
        assert bst.test_method('Adam') == 'Hello Adam'