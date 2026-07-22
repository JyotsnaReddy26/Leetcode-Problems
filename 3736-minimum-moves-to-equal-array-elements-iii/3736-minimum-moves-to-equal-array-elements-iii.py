class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum=max(nums)
        count=0
        for i in range(len(nums)):
            count+=maximum-nums[i]

        return count