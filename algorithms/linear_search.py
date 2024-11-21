class LinearSearch:
    
    def __init__(self):
        return
    
    def __name__(self):
        return 'LinearSearch'
    
    def search_in_array(self, A, p, q, key):
        for i in range (p, q):
            if A[i] == key:
                return i
        return None