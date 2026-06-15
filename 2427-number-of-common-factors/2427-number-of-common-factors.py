class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count=0
        arr1=[]
        arr2=[]
        for i in range(1,a+1):
            if a%i==0:
                arr1.append(i)
        for j in range(1,b+1):
            if b%j==0:
                arr2.append(j)
        for x in arr1:
            if x in arr2:
                count+=1
        return count