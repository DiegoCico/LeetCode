class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        idx = 0
        for i in s:
            if i in d:
                d[i][0] += 1
            else:
                d[i] = [1, idx]
            idx += 1
        
        for k, v in d.items():
            if v[0] == 1: 
                return v[1]
        return -1