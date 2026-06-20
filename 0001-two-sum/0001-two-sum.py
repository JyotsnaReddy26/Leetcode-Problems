class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
       dicto={}
       for i in range(len(nums)):
            wanted=target-nums[i]
            if wanted in dicto:
                return(dicto[wanted],i)
            dicto[nums[i]]=i