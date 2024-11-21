import sys
import time
import random
sys.path.append("../algorithms")
from algorithms.linear_search import LinearSearch
from algorithms.binary_search import BinarySearch

def compare_performance(algorithms_to_compare):
    array_sizes = [10**4, 10**5, 10**6]  # Array sizes to test
    for size in array_sizes:
        print(f"\nArray size: {size}")
        
        # Generate random array
        array = [random.randint(0, 2**32) for _ in range(size)]
        key = array[-1]  # Choose the last value (worst case)
        
        for algorithm in algorithms_to_compare:
            # Test Insertion Sort
            array_copy = array.copy()
            start_time = time.time()
            algorithm.search_in_array(array_copy, 0, len(array_copy), key)
            total_time = time.time() - start_time
            print(algorithm.__name__(), f": {total_time:.6f} seconds")

if __name__ == '__main__':
    compare_performance([LinearSearch(), BinarySearch()])