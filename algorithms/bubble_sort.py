class BubbleSort:
    
    def __init__(self):
        return
    
    def __name__(self):
        return 'BubbleSort'
    
    def sort_array(self, A, p, q):
        for i in range(p, q-1):
            for j in range(q-1, i, -1):
                if A[j] < A[j-1]:
                    A[j], A[j-1] = A[j-1], A[j]