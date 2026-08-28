class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minimum=min(nums)
        maximum=max(nums)
        arr=[]
        for i in range(len(nums)):
            if nums[i]!=maximum and nums[i]!=minimum:
                arr.append(nums[i])
            else:
                arr.append(-1)
        for i in range(len(arr)):
            if arr[i]!=-1:
                return arr[i]
        return -1
    