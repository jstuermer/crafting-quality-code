import a1
import unittest

class TestStockPriceSummary(unittest.TestCase):
    """Test class for function a1.stock_price_summary."""

    def test_stock_price_summary_empty(self):
        """Test for an empty list."""

        act = a1.stock_price_summary([])
        exp = (0.0, 0.0)

        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_negative(self):
        """Test for a list with a negative value."""

        act = a1.stock_price_summary([-1.02])
        exp = (0.0, -1.02)

        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_zero(self):
        """Test for a list with one zero."""

        act = a1.stock_price_summary([0.0])
        exp = (0.0, 0.0)

        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_positive(self):
        """Test for a list with a positive value."""

        act = a1.stock_price_summary([1.02])
        exp = (1.02, 0.0)

        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_positive_negative(self):
        """Test for a list with a positive and a negative value."""

        act = a1.stock_price_summary([1.02, -1.03])
        exp = (1.02, -1.03)

        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_zero_negative(self):
        """Test for a list with a zero and a negative value."""

        act = a1.stock_price_summary([0.0, -1.2])
        exp = (0.0, -1.2)

        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_zero_positive(self):
        """Test for a list with a positive value and a zero."""

        act = a1.stock_price_summary([1.2, 0.0])
        exp = (1.2, 0.0)

        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_negative_large(self):
        """Test for a larger list with only negative values."""

        act = a1.stock_price_summary([-1.02, -0.03, -0.4, -0.1])
        exp = (0.0, -1.55)
        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_zero_large(self):
        """Test for a larger list with only zeros."""

        act = a1.stock_price_summary([0.0, 0.0, 0.0, 0.0])
        exp = (0.0, 0.0)

        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_positive_large(self):
        """Test for a larger list with only positive values."""

        act = a1.stock_price_summary([1.02, 0.03, 0.4, 0.1])
        exp = (1.55, 0.0)

        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_general_large(self):
        """Test for a larger list with negative, positive and zero values."""

        act = a1.stock_price_summary([0.01, -0.02, -0.14, 0, 0, 0.10, -0.01])
        exp = (0.11, -0.17)

        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

if __name__ == '__main__':
    unittest.main(exit=False)
