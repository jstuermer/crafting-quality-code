import unittest
import duplicates

class TestRemoveShared(unittest.TestCase):
    """Tests for function duplicates.remove_shared."""

    def test_general_case(self):
        """
        Test remove_shared for two lists with items that are identical as well
        as items that differ between the two lists.
        """

        list_1 = [1, 2, 3, 4, 5, 6]
        list_2 = [2, 4, 5, 7]

        duplicates.remove_shared(list_1, list_2)

        self.assertEqual(list_1, [1, 3, 6])
        self.assertEqual(list_2, [2, 4, 5, 7])

    def test_empty_list_1(self):
        """
        Test remove_shared for an empty list L1 and a non-empty list L2.
        """

        list_1 = []
        list_2 = [1, 2, 3]

        duplicates.remove_shared(list_1, list_2)

        self.assertEqual(list_1, [])
        self.assertEqual(list_2, [1, 2, 3])

    def test_empty_list_2(self):
        """
        Test remove_shared for a non-empty list L1 and an empty list L2.
        """

        list_1 = [1, 2, 3]
        list_2 = []

        duplicates.remove_shared(list_1, list_2)

        self.assertEqual(list_1, [1, 2, 3])
        self.assertEqual(list_2, [])

if __name__ == '__main__':
    unittest.main(exit=False)
