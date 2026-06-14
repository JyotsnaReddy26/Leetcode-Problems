class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        k={}
        count=0
        for j in range(0,len(stones)):
                if stones[j] in k:
                    k[stones[j]]+=1
                else:
                    k[stones[j]]=1
        for i in range(0,len(jewels)):
            if jewels[i] in k:
                count+=k[jewels[i]]
        return count

                

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    