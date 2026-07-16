class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = {}

        for i in range(1, n + 1):
            num = i
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num //= 10

            if digit_sum in freq:
                freq[digit_sum] += 1
            else:
                freq[digit_sum] = 1

        maximum = max(freq.values())

        count = 0
        for value in freq.values():
            if value == maximum:
                count += 1

        return count