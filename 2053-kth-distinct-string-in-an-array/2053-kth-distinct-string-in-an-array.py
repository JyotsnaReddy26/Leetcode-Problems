class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dicto = {}

        for i in range(len(arr)):
            if arr[i] in dicto:
                dicto[arr[i]] += 1
            else:
                dicto[arr[i]] = 1

        n_arr = []

        for key, value in dicto.items():
            if value == 1:
                n_arr.append(key)

        if len(n_arr) >= k:
            return n_arr[k - 1]

        return ""