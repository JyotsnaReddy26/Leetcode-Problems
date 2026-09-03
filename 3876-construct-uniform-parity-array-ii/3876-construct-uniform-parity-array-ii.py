class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minimum = min(nums1)

        if minimum % 2 == 1:
            return True

        odd_count = 0

        for x in nums1:
            if x % 2 == 1:
                odd_count += 1

        if odd_count == 0:
            return True

        return False