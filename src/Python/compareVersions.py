class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        V1 = version1.split(".")
        V2 = version2.split(".")
        l1 = len(V1)
        l2 = len(V2)
        l3 = (l1, l2, V1, 1) if l1 > l2 else (l2, l1, V2, -1)

        for x1, x2 in zip(V1,V2):
            if int(x1)<int(x2): return -1
            if int(x1)>int(x2): return 1

        for x in range(l3[1], l3[0]):
            print(l3)
            if int(l3[2][x]) > 0:
                return int(l3[3])
        
        return 0
