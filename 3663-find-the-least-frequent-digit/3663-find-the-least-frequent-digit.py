class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = [0] * 10

        while n > 0:
            freq[n % 10] += 1
            n //= 10

        ans = 0
        mn = float("inf")

        for i in range(10):
            if 0 < freq[i] < mn:
                mn = freq[i]
                ans = i

        return ans