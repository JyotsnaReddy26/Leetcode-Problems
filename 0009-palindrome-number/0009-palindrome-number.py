class Solution:
    def isPalindrome(self, x: int) -> bool:
        number=x
        result=0
        while x>0:
            last_digit=x%10
            result=result*10+last_digit
            x//=10
        if number==result:
            return True
        else:
            return False