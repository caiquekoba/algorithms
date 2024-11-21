class BinarySearch:
    
    def __init__(self):
        return
    
    def __name__(self):
        return 'BinarySearch'
    
    def search_in_array(self, A, p, r, key):
        if p >= r:
            return None
        q = (p+r)//2
        if key==A[q]:
            return q
        elif key > A[q]:
            return self.search_in_array(A, q+1, r, key)
        else:
            return self.search_in_array(A, p, q, key)
