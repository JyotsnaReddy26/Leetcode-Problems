class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()

        prod1=(nums[-1]-1)*(nums[-2]-1)
        prod2=(nums[0]-1)*(nums[1]-1)

        return max(prod1,prod2)