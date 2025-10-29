def getPower(x, count):
    if x == 1:
        return count
    elif x % 2 == 0:
        return getPower(x//2, count+1)
    else:
        return getPower(3*x+1, count+1)

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = []
        for i in range(lo, hi+1):
            x = getPower(i, 0)
            arr.append([i,x])
        arr.sort(key=lambda x:x[1])
        print(arr)
        return arr[k-1][0]