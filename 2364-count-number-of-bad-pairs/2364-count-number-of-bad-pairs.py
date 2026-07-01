class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2

        freq = {}
        good_pairs = 0

        for i in range(n):
            key = nums[i] - i

            if key in freq:
                good_pairs += freq[key]

            freq[key] = freq.get(key, 0) + 1

        return total_pairs - good_pairs