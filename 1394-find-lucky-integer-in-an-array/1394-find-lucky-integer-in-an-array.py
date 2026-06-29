class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dicto={}
        for i in range(len(arr)):
            if arr[i] in dicto:
                dicto[arr[i]]+=1
            else:
                dicto[arr[i]]=1
        answer=-1

        for key,value in dicto.items():
            if key==value:
                answer=max(answer,key)
        return answer

