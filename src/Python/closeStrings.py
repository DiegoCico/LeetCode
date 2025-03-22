class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            print("Length mismatch")
            return False

        d1 = {}
        d2 = {}

        for i in word1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1

        for i in word2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1

        print("d1:", d1)
        print("d2:", d2)

        if set(d1.keys()) != set(d2.keys()):
            print("Character sets do not match:", set(d1.keys()), set(d2.keys()))
            return False

        l1 = sorted(d1.values())
        l2 = sorted(d2.values())

        print("Sorted frequencies:")
        print("l1:", l1)
        print("l2:", l2)

        return l1 == l2
