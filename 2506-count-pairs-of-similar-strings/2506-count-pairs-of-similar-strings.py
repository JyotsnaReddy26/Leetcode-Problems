class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                original=set(words[i])
                wanted=set(words[j])
                if original==wanted:
                    count+=1
        return count