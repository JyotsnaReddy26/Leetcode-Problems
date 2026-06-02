class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dicto_s={}
        dicto_t={}
        for j,r in zip(s,t):
            if j in dicto_s:
                if dicto_s[j]!=r:
                    return False
            else:
                dicto_s[j]=r
            if r in dicto_t:
                if dicto_t[r]!=j:
                    return False
            else:
                dicto_t[r]=j
        return True