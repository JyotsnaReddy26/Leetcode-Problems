class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        new_set=set(nums)
        for i in range(1,len(nums)+1):
            if i not in new_set:
                ans.append(i)
        return ans

