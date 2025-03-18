class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0
        for g in gain:
            altitude += g
            if highest < altitude:
                highest = altitude

        return highest