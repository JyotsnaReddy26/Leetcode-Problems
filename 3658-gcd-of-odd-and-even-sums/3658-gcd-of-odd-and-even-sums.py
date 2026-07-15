import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd=0
        sumeven=0

        even=2
        odd=1

        for i in range(n):
                sumeven+=even
                sumodd+=odd
                even+=2
                odd+=2
        return math.gcd(sumeven,sumodd)