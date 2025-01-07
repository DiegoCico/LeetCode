class Solution(object):
    def stringShift(self, s, shift):
        N = len(s)
        start = 0
        for direction, amount in shift:
            direction = -1 if direction == 0 else 1
            start = (start - amount * direction) % N
            if start < 0:
                start += N
            elif start >= N:
                start -= N
        return s[start:] + s[:start]