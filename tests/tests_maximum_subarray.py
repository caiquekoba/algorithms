import sys
import time
import unittest
sys.path.append("../algorithms")
from algorithms.maximum_subarray import MaxSubarray

class TestMaxSubarray(unittest.TestCase):

    def setUp(self):
        """Set up an instance of MaxSubarray for testing."""
        self.max_subarray = MaxSubarray()

    def test_max_crossing_subarray(self):
        """Test the max_crossing_subarray method."""
        A = [-2, -3, 4, -1, -2, 1, 5, -3]
        result = self.max_subarray.max_crossing_subarray(A, 0, 3, 7)
        expected = (2, 6, 7)  # The crossing subarray [4, -1, -2, 1, 5]
        self.assertEqual(result, expected)

    def test_maximum_subarray(self):
        """Test the maximum_subarray method."""
        A = [-2, -3, 4, -1, -2, 1, 5, -3]
        result = self.max_subarray.maximum_subarray(A, 0, len(A) - 1)
        expected = (2, 6, 7)  # The maximum subarray [4, -1, -2, 1, 5]
        self.assertEqual(result, expected)

    def test_maximum_subarray_single_element(self):
        """Test the maximum_subarray method with a single-element array."""
        A = [42]
        result = self.max_subarray.maximum_subarray(A, 0, 0)
        expected = (0, 0, 42)  # The single-element subarray
        self.assertEqual(result, expected)

    def test_maximum_subarray_all_negative(self):
        """Test the maximum_subarray method with an all-negative array."""
        A = [-8, -3, -6, -2, -5, -4]
        result = self.max_subarray.maximum_subarray(A, 0, len(A) - 1)
        expected = (3, 3, -2)  # The least negative single-element subarray
        self.assertEqual(result, expected)

    def test_maximum_subarray_all_zeros(self):
        """Test the maximum_subarray method with an array of all zeros."""
        A = [0, 0, 0, 0, 0]
        result = self.max_subarray.maximum_subarray(A, 0, len(A) - 1)
        expected = (0, 0, 0)  # Any single zero is a valid maximum subarray
        self.assertEqual(result, expected)

    def test_maximum_subarray_alternating_signs(self):
        """Test the maximum_subarray method with alternating signs."""
        A = [1, -1, 2, -2, 3, -3, 4, -4]
        result = self.max_subarray.maximum_subarray(A, 0, len(A) - 1)
        expected = (6, 6, 4)  # The single-element subarray [4]
        self.assertEqual(result, expected)

    def test_maximum_subarray_entire_array(self):
        """Test the maximum_subarray method where the maximum subarray is the entire array."""
        A = [2, 3, 1, 5]
        result = self.max_subarray.maximum_subarray(A, 0, len(A) - 1)
        expected = (0, 3, 11)  # The entire array [2, 3, 1, 5]
        self.assertEqual(result, expected)

    def test_maximum_subarray_empty_array(self):
        """Test the maximum_subarray method with an empty array."""
        A = []
        with self.assertRaises(AssertionError):
            self.max_subarray.maximum_subarray(A, 0, len(A) - 1)

if __name__ == '__main__':
    unittest.main(verbosity=1)