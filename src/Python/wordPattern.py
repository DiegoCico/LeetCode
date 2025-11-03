class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split()
        if len(pattern) != len(list_s):
            return False

        d = {}
        used = set()

        for p, w in zip(pattern, list_s):
            if p in d:
                if d[p] != w:
                    return False
            else:
                if w in used:  
                    return False
                d[p] = w
                used.add(w)
        return True
