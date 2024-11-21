class InsertionSort:
    
    def __init__(self):
        return
    
    def __name__(self):
        return 'InsertionSort'
    
    def sort_array(self, A, p, q):
        for j in range (p+1, q):
            key = A[j]
            i = j-1
            while i >= 0 and A[i] > key:
                A[i+1] = A[i]
                i -= 1
            A[i+1] = key

