class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        arr=[]
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for key,value in freq.items():
            if value>(len(nums)//3):
                arr.append(key)
        return arr