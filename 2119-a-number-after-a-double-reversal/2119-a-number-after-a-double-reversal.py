class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        original=num
        reverse=0
        while num>0:
            k=num%10
            num//=10
            reverse=reverse*10+k
        reverse2=0
        while reverse>0:
            m=reverse%10
            reverse//=10
            reverse2=reverse2*10+m
        if original==reverse2:
            return True
        return False