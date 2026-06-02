class Solution:
    def isPalindrome(self, x: int) -> bool:
        strs=str(x)
        i=0
        j=len(strs)-1
        while i<=j:
            if strs[i]!=strs[j]:
                return False
            i+=1
            j-=1
        return True