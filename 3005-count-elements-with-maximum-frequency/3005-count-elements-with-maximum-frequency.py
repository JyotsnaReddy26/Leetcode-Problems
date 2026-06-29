class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dicto={}
        for i in range(len(nums)):
            if nums[i] in dicto:
                dicto[nums[i]]+=1
            else:
                dicto[nums[i]]=1
        count=0
        maxi=max(dicto.values())
        for key,value in dicto.items():
            if value==maxi:
                count+=value
        return count