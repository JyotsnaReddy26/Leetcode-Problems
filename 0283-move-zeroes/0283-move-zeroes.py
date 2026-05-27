class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=[]
        for i in range(len(nums)):
            if nums[i]==0:
                arr.append(nums[i])
        while 0 in nums:
            nums.remove(0)
        nums[:]=nums+arr
        print(nums)
                
        