class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count=0
        for i in range(len(nums)):
            digit_count=0
            while nums[i]>0:
                last_digit=nums[i]%10
                digit_count+=1
                nums[i]//=10
            if digit_count%2==0:
                even_count+=1
        return even_count
