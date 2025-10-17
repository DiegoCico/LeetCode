def getPower(x):
    if x == 1:
        return 0
    if x % 2 == 0:
        return 1 + getPower(x / 2)
    else:
        return 1 + getPower(3 * x + 1)

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        for i in range(lo, hi+1):
            i_pow = getPower(i)
            res.append((i_pow, i))
        res = sorted(res, key=lambda x: x[0])
        return res[k-1][1]