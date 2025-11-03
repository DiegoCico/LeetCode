class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i + 1 for i in range(n)]  
        i = 0

        while len(arr) > 1:
            i = (i + k - 1) % len(arr)   
            del arr[i]                 
        return arr[0]
