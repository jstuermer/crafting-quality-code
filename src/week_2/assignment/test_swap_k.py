import a1
import unittest

class TestSwapK(unittest.TestCase):
    """Test class for function a1.swap_k."""

    def test_swap_k_empty(self):
        """Test for empty list (no swapping possible)."""

        nums = []
        a1.swap_k(nums, 0)

        self.assertEqual(nums, [])

    def test_swap_k_one(self):
        """Test for a list with one item (no swapping possible)."""

        nums = [1]
        a1.swap_k(nums, 0)

        self.assertEqual(nums, [1])

    def test_swap_k_two_no_swap(self):
        """Test for a list with two items and no swapping."""

        nums = [1, 2]
        a1.swap_k(nums, 0)

        self.assertEqual(nums, [1, 2])

    def test_swap_k_two_swap(self):
        """Test for a list with two items and swapping."""

        nums = [1, 2]
        a1.swap_k(nums, 1)

        self.assertEqual(nums, [2, 1])

    def test_swap_k_large_even_no_swap(self):
        """
        Test for a larger list with an even number of items and no swapping.
        """

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 0)

        self.assertEqual(nums, [1, 2, 3, 4, 5, 6])

    def test_swap_k_large_even_swap(self):
        """Test for a larger list with an even number of items and swapping."""

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)

        self.assertEqual(nums, [5, 6, 3, 4, 1, 2])

    def test_swap_k_large_even_max_swap(self):
        """
        Test for a larger list with an even number of items and swapping the
        maximum possible number of items.
        """

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 3)

        self.assertEqual(nums, [4, 5, 6, 1, 2, 3])

    def test_swap_k_large_odd_no_swap(self):
        """
        Test for a larger list with an odd number of items and no swapping.
        """

        nums = [1, 2, 3, 4, 5, 6, 7]
        a1.swap_k(nums, 0)

        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7])

    def test_swap_k_large_odd_swap(self):
        """Test for a larger list with an odd number of items and swapping."""

        nums = [1, 2, 3, 4, 5, 6, 7]
        a1.swap_k(nums, 2)

        self.assertEqual(nums, [6, 7, 3, 4, 5, 1, 2])

    def test_swap_k_large_odd_max_swap(self):
        """
        Test for a larger list with an odd number of items and swapping the
        maximum possible number of items.
        """

        nums = [1, 2, 3, 4, 5, 6, 7]
        a1.swap_k(nums, 3)

        self.assertEqual(nums, [5, 6, 7, 4, 1, 2, 3])

if __name__ == '__main__':
    unittest.main(exit=False)
