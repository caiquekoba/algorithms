import sys
import time
import unittest
sys.path.append("../algorithms")
from algorithms.selection_sort import SelectionSort

class TestSelectionSort(unittest.TestCase):

    def setUp(self):
        # Instantiate the InsertionSort class
        self.sorter = SelectionSort()
        # Start timing the test
        self.start_time = time.time()

    def tearDown(self):
        # End timing and print the execution time
        elapsed_time = time.time() - self.start_time
        print(f"{self.id()} took {elapsed_time:.6f} seconds")

    def test_sort_sub_array_full_array(self):
        """Test sorting the entire array"""
        A = [5, 2, 9, 1, 5, 6]
        self.sorter.sort_array(A, 0, len(A))
        self.assertEqual(A, [1, 2, 5, 5, 6, 9])

    def test_sort_sub_array_partial_array(self):
        """Test sorting a subarray within a larger array"""
        A = [3, 1, 4, 1, 5, 9, 2]
        self.sorter.sort_array(A, 2, 5)
        self.assertEqual(A, [3, 1, 1, 4, 5, 9, 2])  # Only indices 2 to 4 are sorted

    def test_sort_sub_array_empty_array(self):
        """Test sorting an empty array"""
        A = []
        self.sorter.sort_array(A, 0, 0)
        self.assertEqual(A, [])

    def test_sort_sub_array_single_element(self):
        """Test sorting an array with a single element"""
        A = [1]
        self.sorter.sort_array(A, 0, 1)
        self.assertEqual(A, [1])

    def test_sort_sub_array_sorted_array(self):
        """Test sorting an already sorted array"""
        A = [1, 2, 3, 4, 5]
        self.sorter.sort_array(A, 0, len(A))
        self.assertEqual(A, [1, 2, 3, 4, 5])

    def test_sort_sub_array_reverse_sorted(self):
        """Test sorting a reverse sorted array"""
        A = [5, 4, 3, 2, 1]
        self.sorter.sort_array(A, 0, len(A))
        self.assertEqual(A, [1, 2, 3, 4, 5])

    def test_sort_sub_array_large_n(self):
        """Test sorting with n and m close to the array's end"""
        A = [4, 3, 1, 5, 2]
        self.sorter.sort_array(A, 3, 5)
        self.assertEqual(A, [4, 3, 1, 2, 5])  # Only sorts last two elements

    def test_sort_sub_array_out_of_bounds(self):
        """Test handling when m is greater than array length"""
        A = [4, 3, 1, 5, 2]
        with self.assertRaises(IndexError):
            self.sorter.sort_array(A, 1, 10)

if __name__ == '__main__':
    unittest.main(verbosity=1)