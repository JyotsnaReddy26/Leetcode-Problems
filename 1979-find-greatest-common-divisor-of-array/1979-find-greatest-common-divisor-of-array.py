import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
    
            maximum=max(nums)
            minimum=min(nums)
            return math.gcd(maximum,minimum)