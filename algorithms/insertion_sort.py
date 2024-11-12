class InsertionSort:
    
    def __init__(self):
        return
    
    def sort_sub_array(self, A, n, m):
        for j in range (n+1, m):
            key = A[j]
            i = j-1
            while i >= 0 and A[i] > key:
                A[i+1] = A[i]
                i -= 1
            A[i+1] = key

