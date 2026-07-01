class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pair_count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    pair_count+=1
        return pair_count
