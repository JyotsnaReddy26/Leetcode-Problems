class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num % 2 == 0:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1

        if len(freq) == 0:
            return -1

        maximum = 0
        answer = 0

        for key, value in freq.items():
            if value > maximum:
                maximum = value
                answer = key
            elif value == maximum and key < answer:
                answer = key

        return answer 