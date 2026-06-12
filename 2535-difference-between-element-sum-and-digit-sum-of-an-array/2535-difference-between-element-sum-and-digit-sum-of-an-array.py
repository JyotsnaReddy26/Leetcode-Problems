class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum=sum(nums)
        digit_sum=0
        for i in range(len(nums)):
            while nums[i]>0:
                last_digit=nums[i]%10
                digit_sum+=last_digit
                nums[i]//=10
        return abs(element_sum-digit_sum)