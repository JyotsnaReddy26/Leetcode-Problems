class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sumi=0
        while n>0:
            last_digit=n%10
            product*=last_digit
            sumi+=last_digit
            n//=10
        return product-sumi