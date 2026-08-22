class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=min(nums)
        n=max(nums)
        arr=[]
        
        for i in range(m,n+1):
            if i not in nums:
                arr.append(i)
        return arr
