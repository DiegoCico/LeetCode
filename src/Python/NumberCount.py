class Solution:
    def numberCount(self, a: int, b: int) -> int:
        c = 0
        for i in range(a,b+1): 
            if self.is_unquie(i):
                c += 1
        return c
        
    def is_unquie(self, num):
        digits = list(str(num)) 
        A = []
        for i in digits: 
            if i in A:
                return False
            A.append(i)
        return True