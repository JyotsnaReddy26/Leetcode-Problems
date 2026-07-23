class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        freq={}
        for i in range(0,len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for i in freq:
            if freq[i]>n//2:
                return i