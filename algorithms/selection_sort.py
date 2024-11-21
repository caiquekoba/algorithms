class SelectionSort:
    
    def __init__(self):
        return
    
    def __name__(self):
        return 'SelectionSort'
    
    def sort_array(self, A, p, q):
        for i in range(p, q-1):
            id = i
            for j in range(i+1, q):
                if A[j] < A[id]:
                    id = j
            A[i], A[id] = A[id], A[i]