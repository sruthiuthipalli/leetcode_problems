class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}
        for b in s:
            f[b]=f.get(b,0)+1
        for a,b in enumerate(s):
            if f[b]==1:
                return a
        return -1        
        