class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dicto={}
        for i in range(len(nums)):
            if nums[i] in dicto:
                dicto[nums[i]]+=1
            else:
                dicto[nums[i]]=1
        for key,value in dicto.items():
            if value>1:
                return True
        return False