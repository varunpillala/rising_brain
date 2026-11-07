class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pos = len(nums)
        while(left<=right):
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                pos = mid
                right = mid - 1
            else:
                left = mid + 1
        return pos
        