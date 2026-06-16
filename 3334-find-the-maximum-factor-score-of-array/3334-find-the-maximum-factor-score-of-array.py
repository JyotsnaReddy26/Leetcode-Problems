from math import gcd
from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)

        n = len(nums)
        suf_gcd = [0] * (n + 1)
        suf_lcm = [1] * (n + 1)

        for i in range(n - 1, -1, -1):
            suf_gcd[i] = gcd(suf_gcd[i + 1], nums[i])
            suf_lcm[i] = lcm(suf_lcm[i + 1], nums[i])

        ans = suf_gcd[0] * suf_lcm[0]

        pre_gcd = 0
        pre_lcm = 1

        for i in range(n):
            g = gcd(pre_gcd, suf_gcd[i + 1])
            l = lcm(pre_lcm, suf_lcm[i + 1])
            ans = max(ans, g * l)
            pre_gcd = gcd(pre_gcd, nums[i])
            pre_lcm = lcm(pre_lcm, nums[i])

        return ans