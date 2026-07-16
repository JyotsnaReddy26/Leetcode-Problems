import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx=[]
        max_element=nums[0]
        for i in nums:
            max_element=max(max_element,i)
            mx.append(max_element)
        pre=[]
        for j in range(len(mx)):
            pre.append(math.gcd(mx[j],nums[j]))
        
        pre.sort()
        sum=0
        for i in range(len(pre)//2):
           sum+=math.gcd(pre[i],pre[len(pre)-1-i])
        #if len(pre)%2==1:
            #sum-=pre[len(pre)//2]
        return sum



            
