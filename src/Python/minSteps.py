class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic = defaultdict(int)

        for i in range(len(s)):
            dic[s[i]] += 1
            dic[t[i]] -= 1
        
        s = 0
        for v in dic.values():
            if v < 0:
                s += abs(v)

        return s