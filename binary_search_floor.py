class Solution:
    def findFloor(self, arr, x):
        # code here
        left = 0
        right = len(arr) - 1
        floor = -1
        while(left <= right):
            mid = left + (right - left) // 2
            if arr[mid] <= x: #lower bound
                floor = mid
                left = mid +1
            else:
                right = mid - 1
        return floor