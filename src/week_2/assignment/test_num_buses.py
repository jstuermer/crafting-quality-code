import a1
import unittest

class TestNumBuses(unittest.TestCase):
    """Test class for function a1.num_buses."""

    def test_num_buses_zero(self):
        """Test for no people."""

        act = a1.num_buses(0)
        exp = 0

        self.assertEqual(act, exp)

    def test_num_buses_one(self):
        """Test for one person."""

        act = a1.num_buses(1)
        exp = 1

        self.assertEqual(act, exp)

    def test_num_buses_at_boundary_1(self):
        """Test for 50 people (the maximum capacity of a bus)."""

        act = a1.num_buses(50)
        exp = 1

        self.assertEqual(act, exp)

    def test_num_buses_above_boundary_1(self):
        """Test for 51 people."""

        act = a1.num_buses(51)
        exp = 2

        self.assertEqual(act, exp)

    def test_num_buses_at_boundary_2(self):
        """Test for 100 people (double the maximum capacity of a bus)."""

        act = a1.num_buses(100)
        exp = 2

        self.assertEqual(act, exp)

    def test_num_buses_large(self):
        """Test for a large number of people."""

        act = a1.num_buses(1025)
        exp = 21

        self.assertEqual(act, exp)

if __name__ == '__main__':
    unittest.main(exit=False)
