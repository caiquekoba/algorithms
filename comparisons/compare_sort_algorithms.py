import sys
import time
import random
sys.path.append("../algorithms")
from algorithms.merge_sort import MergeSort
from algorithms.insertion_sort import InsertionSort
from algorithms.selection_sort import SelectionSort
from algorithms.bubble_sort import BubbleSort

def compare_performance(algorithms_to_compare):
    array_sizes = [10**3, 10**4, 10**5]  # Array sizes to test
    for size in array_sizes:
        print(f"\nArray size: {size}")
        
        # Generate random array
        array = [random.randint(0, 2**32) for _ in range(size)]
        
        for algorithm in algorithms_to_compare:
            # Test Insertion Sort
            array_copy = array.copy()
            start_time = time.time()
            algorithm.sort_array(array_copy, 0, len(array_copy))
            total_time = time.time() - start_time
            print(algorithm.__name__(), f": {total_time:.6f} seconds")

if __name__ == '__main__':
    compare_performance([InsertionSort(), MergeSort(), SelectionSort(), BubbleSort()])