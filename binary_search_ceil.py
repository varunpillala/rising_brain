class Solution:
    def findCeil(self, arr, x):
        # code here
        left = 0
        right = len(arr) - 1
        ceil = -1
        while(left<=right):
            mid = left + (right - left) // 2
            if arr[mid] >= x: #upper bound
                ceil = mid
                right = mid -1
            else:
                left = mid + 1
        return ceil