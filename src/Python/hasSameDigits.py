class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 2 and s[0] == s[1]:
            return True
        if len(s) < 2:
            return False
        new_s = ""
        
        for i in range(1, len(s)):
            new_s += str((int(s[i-1]) + int(s[i])) % 10)
        
        return self.hasSameDigits(new_s)