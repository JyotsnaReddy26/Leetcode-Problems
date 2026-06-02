class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dicto={}
        t_dicto={}
        for i in range(len(s)):
            if s[i] in s_dicto:
                s_dicto[s[i]]+=1
            else:
                s_dicto[s[i]]=1
        for i in range(len(t)):
            if t[i] in t_dicto:
                t_dicto[t[i]]+=1
            else:
                t_dicto[t[i]]=1
        if s_dicto==t_dicto:
            return True
        else:
            return False