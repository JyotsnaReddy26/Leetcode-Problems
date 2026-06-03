class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicto={}
        for i in range(len(nums)):
            if nums[i] in dicto:
                dicto[nums[i]]+=1
            else:
                dicto[nums[i]]=1
        sorted_dict=sorted(dicto.items(),key=lambda x:x[1],reverse=True)
        arr=[]
        for i in range(k):
            arr.append(sorted_dict[i][0])
        return arr
    