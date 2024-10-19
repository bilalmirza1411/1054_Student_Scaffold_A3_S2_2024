from __future__ import annotations

from typing import List, Tuple, TypeVar

from data_structures.bst import BinarySearchTree
from algorithms import mergesort
K = TypeVar('K')
I = TypeVar('I')
class TreeNode:
    def __init__(self, key: K, item: I):
        self.key = key
        self.item = item
        self.left = None
        self.right = None

class BetterBST(BinarySearchTree[K, I]):
    def __init__(self, elements: List[Tuple[K, I]]) -> None:
        """
        Initialiser for the BetterBST class.
        We assume that the all the elements that will be inserted
        into the tree are contained within the elements list.

        As such you can assume the length of elements to be non-zero.
        The elements list will contain tuples of key, item pairs.

        First sort the elements list and then build a balanced tree from the sorted elements
        using the corresponding methods below.

        Args:
            elements(List[tuple[K, I]]): The elements to be inserted into the tree.

        Complexity:
            Best Case Complexity: O(nlogn), where n is the number of elements in the input / the final number of nodes in the tree.
            Worst Case Complexity: O(nlogn)
        """
        super().__init__()
        new_elements: List[Tuple[K, I]] = self.__sort_elements(elements)
        self.__build_balanced_tree(new_elements)

    def __sort_elements(self, elements: List[Tuple[K, I]]) -> List[Tuple[K, I]]:
        """
        Recall one of the drawbacks to using a binary search tree is that it can become unbalanced.
        If we know the elements ahead of time, we can sort them and then build a balanced tree.
        This will help us maintain the O(log n) complexity for searching, inserting, and deleting elements.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to sort.

        Returns:
            list(Tuple[K, I]]) - elements after being sorted.

        Complexity:
            Best Case Complexity: O(nlogn), where n is the number of elements in the input / the final number of nodes in the tree.
            Worst Case Complexity: O(nlogn), where n is the number of elements in the input / the final number of nodes in the tree.
        """
        sorted_elements = mergesort(elements, lambda x: x[0])
        return [item for x, item in sorted_elements]

    def __build_balanced_tree(self, elements: List[Tuple[K, I]]) -> None:
        """
        This method will build a balanced binary search tree from the sorted elements.

        Args:
            elements (List[Tuple[K, I]]): The elements we wish to use to build our balanced tree.

        Returns:
            None

        Complexity:
            (This is the actual complexity of your code, 
            remember to define all variables used.)
            Best Case Complexity: TODO
            Worst Case Complexity: TODO

        Justification:
            TODO

        Complexity requirements for full marks:
            Best Case Complexity: O(n * log(n))
            Worst Case Complexity: O(n * log(n))
            where n is the number of elements in the list.
        """
        if not elements:
            return None
        
        # Find the middle element to ensure balance
        mid_index = len(elements) // 2
        mid_element = elements[mid_index]
        
        # Create a new tree node with the middle element
        node = TreeNode(mid_element[0], mid_element[1])
        
        # Recursively build the left and right subtrees
        node.left = self.__build_tree_recursive(elements[:mid_index])
        node.right = self.__build_tree_recursive(elements[mid_index + 1:])
        
        return node
