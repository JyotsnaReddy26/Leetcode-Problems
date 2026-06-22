class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        splitted=[]
        for i in words:
            required=i.split(separator)
            for wanted in required:
                if wanted:
                    splitted.append(wanted)
        return splitted
