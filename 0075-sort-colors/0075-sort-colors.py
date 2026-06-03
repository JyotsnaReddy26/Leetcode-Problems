class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=[]
        z_count=0
        o_count=0
        t_count=0
        for i in range(len(nums)):
            if nums[i]==0:
                z_count+=1
            elif nums[i]==1:
                o_count+=1
            else:
                t_count+=1
        nums[:]=[0]*z_count+[1]*o_count+[2]*t_count
        return nums
