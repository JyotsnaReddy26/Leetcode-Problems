class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        suffix_sum = nums[-1]
        ans = 0

        for i in range(n - 2, -1, -1):
            right_count = n - i - 1

            if nums[i] * right_count > suffix_sum:
                ans += 1

            suffix_sum += nums[i]

        return ans 