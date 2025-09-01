class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        a = n
        while True: 
            split = map(int, str(a))
            summ = 0
            for i in split:
                summ += (i**2)

            if summ == 1: 
                return True
            elif summ in seen: 
                return False
            
            a = summ
            seen.append(a)
        return False