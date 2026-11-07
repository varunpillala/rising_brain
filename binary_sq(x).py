class Solution:
    def floorSqrt(self, n): 
        # code here
        left = 0
        right = n
        res = 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= n:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res