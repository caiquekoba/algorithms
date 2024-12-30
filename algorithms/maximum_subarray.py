class MaxSubarray:
    
    def __init__(self):
        return
    
    def __name__(self):
        return 'MaxSubarray'
    
    def max_crossing_subarray(self, A, p, q, r):
        '''
        Considering A[q] the middle value of the array A. This function returns the subarray passing through A[q] with the highest sum.
        '''
        l_sum = r_sum = -float('inf')
        sum = 0
        for i in range(q,p-1,-1):
            sum = sum + A[i]
            if sum > l_sum:
                l_sum = sum
                max_left = i
        sum = 0
        for j in range(q+1,r+1):
            sum = sum + A[j]
            if sum > r_sum:
                r_sum = sum
                max_right = j
        return (max_left, max_right, l_sum+r_sum)

    def maximum_subarray(self, A, p, r):
        if r < 0:
            r = len(A) + r
            assert 0 <= r < len(A)
        if p == r:
            return (p, r, A[p])
        else:
            q = (p+r)//2
            (l_low, l_high, l_sum) = self.maximum_subarray(A, p, q)
            (r_low, r_high, r_sum) = self.maximum_subarray(A, q+1, r)
            (c_low, c_high, c_sum) = self.max_crossing_subarray(A, p, q, r)
            if l_sum >= r_sum and l_sum >= c_sum:
                return(l_low, l_high, l_sum)
            elif r_sum >= l_sum and r_sum >= c_sum:
                return(r_low, r_high, r_sum)
            else:
                return(c_low, c_high, c_sum)