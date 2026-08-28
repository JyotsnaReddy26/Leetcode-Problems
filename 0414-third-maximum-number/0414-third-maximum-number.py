class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        arr = []

        for i in nums:
            if i not in arr:
                arr.append(i)

        if len(arr) >= 3:
            return arr[2]
        else:
            return arr[0]