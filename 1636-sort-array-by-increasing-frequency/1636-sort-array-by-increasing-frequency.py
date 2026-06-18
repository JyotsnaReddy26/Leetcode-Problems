class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dicto={}
        for i in range(len(nums)):
            if nums[i] in dicto:
                dicto[nums[i]]+=1
            else:
                dicto[nums[i]]=1
        nums.sort(key=lambda x: (dicto[x], -x))
        return nums