class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        i = 0
        n = len(s)
        
        while i < n:
           
            if i + 2 < n and s[i + 2] == '#':
                
                val = int(s[i:i+2])
                
                res.append(chr(96 + val))
                i += 3
            else:
                
                val = int(s[i])
               
                res.append(chr(96 + val))
                i += 1
                
        return "".join(res)
