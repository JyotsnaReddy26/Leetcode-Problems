class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        sum1 = 0
        sum2 = 0

        for i in range(k):
            sum1 += nums[i]
            sum2 += nums[-(i + 1)]

        return abs(sum1 - sum2)