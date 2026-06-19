class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        chars = list(freq.keys())

        for i in range(len(chars)):
            for j in range(i + 1, len(chars)):
                if freq[chars[i]] < freq[chars[j]]:
                    chars[i], chars[j] = chars[j], chars[i]
        result = ""

        for ch in chars:
            result += ch * freq[ch]

        return result