class Solution:
    def countDigits(self, num: int) -> int:
        number=num
        count=0
        while num>0:
            k=num%10
            num//=10
            if number%k==0 and k!=0:
                count+=1
       
        return count