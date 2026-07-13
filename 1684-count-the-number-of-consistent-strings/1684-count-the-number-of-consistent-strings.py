class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        original=set(allowed)
        count=0
        for i in range(len(words)):
            wanted=set(words[i])
            if wanted.issubset(original):
                count+=1
        return count