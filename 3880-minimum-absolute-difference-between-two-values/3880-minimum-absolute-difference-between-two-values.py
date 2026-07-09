class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        INF = float('inf')
        ans = INF

        
        last_one = -INF
        for i in range(n):
            if nums[i] == 1:
                last_one = i
            elif nums[i] == 2 and last_one != -INF:
                ans = min(ans, i - last_one)

        last_one = INF
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                last_one = i
            elif nums[i] == 2 and last_one != INF:
                ans = min(ans, last_one - i)

        return -1 if ans == INF else ans