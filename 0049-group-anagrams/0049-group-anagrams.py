class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicto={}
        for i in strs:
            key=''.join(sorted(i))
            if key not in dicto:
                dicto[key]=[]
            dicto[key].append(i)
        return list(dicto.values())