class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        arr=[]
        dicto={}
        for i in range(len(nums)):
            if nums[i] in dicto:
                dicto[nums[i]]+=1
            else:
                dicto[nums[i]]=1
        for key,value in dicto.items():
            if value==2:
                arr.append(key)
        return arr