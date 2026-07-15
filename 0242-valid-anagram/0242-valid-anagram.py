class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        new_1=sorted(s)
        new_2=sorted(t)
        if new_1==new_2:
            return True
        else:
            return False