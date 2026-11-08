class Solution:
    def missingNum(self, arr: list[int]) -> int:
        # code here
        n = len(arr)
        sum1 = ((n+2) * (n+1)) // 2
        sum2 = 0
        for i in range(n):
            sum2 += arr[i]
            
        return (sum1-sum2)