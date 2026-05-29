class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        l=0
        maxi=1
        for i in range(1,len(s)):
            if ord(s[i])==ord(s[i-1])+1:
                continue
            else:
                maxi=max(maxi,i-l)
                l=i
        maxi=max(maxi,len(s)-l)
        return maxi