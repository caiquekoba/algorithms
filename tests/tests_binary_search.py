import sys
import time
import unittest
sys.path.append("../algorithms")
from algorithms.binary_search import BinarySearch

# Unit tests for LinearSearch
class TestBinarySearch(unittest.TestCase):
    
    def setUp(self):
        """Set up a BinarySearch instance before each test."""
        self.searcher = BinarySearch()
        # Start timing the test
        self.start_time = time.time()

    def tearDown(self):
        # End timing and print the execution time
        elapsed_time = time.time() - self.start_time
        print(f"{self.id()} took {elapsed_time:.6f} seconds")

    def test_key_found(self):
        """Test when the key is present in the array."""
        A = [1, 3, 5, 7, 9]
        result = self.searcher.search_in_array(A, 0, len(A), 5)
        self.assertEqual(result, 2)

    def test_key_not_found(self):
        """Test when the key is not present in the array."""
        A = [1, 3, 5, 7, 9]
        result = self.searcher.search_in_array(A, 0, len(A), 4)
        self.assertIsNone(result)

    def test_key_at_start(self):
        """Test when the key is at the start of the range."""
        A = [1, 3, 5, 7, 9]
        result = self.searcher.search_in_array(A, 0, len(A), 1)
        self.assertEqual(result, 0)

    def test_key_at_end(self):
        """Test when the key is at the end of the range."""
        A = [1, 3, 5, 7, 9]
        result = self.searcher.search_in_array(A, 0, len(A), 9)
        self.assertEqual(result, 4)

    def test_empty_array(self):
        """Test when the array is empty."""
        A = []
        result = self.searcher.search_in_array(A, 0, len(A), 1)
        self.assertIsNone(result)

    def test_partial_range(self):
        """Test when searching within a partial range of the array."""
        A = [1, 3, 5, 7, 9]
        result = self.searcher.search_in_array(A, 1, 4, 7)
        self.assertEqual(result, 3)

    def test_partial_range_not_found(self):
        """Test when the key is outside the partial range."""
        A = [1, 3, 5, 7, 9]
        result = self.searcher.search_in_array(A, 1, 4, 9)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main(verbosity=1)