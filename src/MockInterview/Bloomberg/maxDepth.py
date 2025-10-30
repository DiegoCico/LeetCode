class Solution:
    def maxDepth(self, s: str) -> int:
        open = 0
        maxx = 0
        for i in s: 
            if i == "(":
                open += 1 
            if i == ")":
                maxx = max(open, maxx)
                open -= 1
                
        return maxx