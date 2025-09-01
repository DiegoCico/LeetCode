from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        n = len(senate)
        R = deque()
        D = deque()

        for i, s in enumerate(senate):
            if s == "R":
                R.append(i)
            else:
                D.append(i)

        while R and D:
            r = R.popleft()
            d = D.popleft()
            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)

        return "Radiant" if R else "Dire"
