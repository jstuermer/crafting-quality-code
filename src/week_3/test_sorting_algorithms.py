import sorting_algorithms
import unittest


class TestBubbleSort(unittest.TestCase):
    """Tests for sorting_algorithms.bubble_sort."""

    def test_bubble_sort_empty(self):
        """Test bubble_sort with an empty list."""

        L = []
        sorting_algorithms.bubble_sort(L)
        self.assertEqual(L, [])


class TestSelectionSort(unittest.TestCase):
    """Tests for sorting_algorithms.selection_sort."""

    def test_selection_sort_empty(self):
        """Test selection_sort with an empty list."""

        L = []
        sorting_algorithms.selection_sort(L)
        self.assertEqual(L, [])


if __name__ == "__main__":
    unittest.main(exit=False)
