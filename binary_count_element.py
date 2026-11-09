class Solution:
    def countFreq(self, arr, target):
        # code here
        left = 0
        right = len(arr) - 1
        first = len(arr)
        last = -1
        while(left<= right):
            mid = left + (right-left) // 2
            if arr[mid] >= target:
                if arr[mid] == target:
                    first = mid
                right = mid - 1
            else:
                left = mid + 1
                
        left = 0
        right = len(arr) - 1
        while(left<= right):
            mid = left + (right-left) // 2
            if arr[mid] <= target:
                if arr[mid] == target:
                   last = mid
                left = mid + 1
            else:
                right = mid-1
        if first == len(arr):
            return 0
        return (last + 1 - first)