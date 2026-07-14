class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq={}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
        counts=list(freq.values())
        if len(set(counts))==1:
            return True
        else:
            return False
