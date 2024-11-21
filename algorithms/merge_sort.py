class MergeSort:
    
    def __init__(self):
        return
    
    def __name__(self):
        return 'MergeSort'
    
    def merge_sorted_sub_arrays(self, A, p, q, r):
        '''
        Considering A[p:q] and A[q:r] sorted sub-arrays, this function returns A[p:r] sorted
        '''
        L = A[p:q]+[float('inf')]
        R = A[q:r]+[float('inf')]
        i = j = 0
        for k in range(p,r):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

    def sort_array(self, A, p, r):
        if p+1 < r:
            q = (p+r)//2
            self.sort_array(A, p, q)
            self.sort_array(A, q, r)
            self.merge_sorted_sub_arrays(A, p, q, r)