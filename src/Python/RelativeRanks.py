class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        copy = self.convert_to_string(score)
        for i in range(len(score)):
            index = score.index(max(score))
            score[index] = -1
            if i == 0:
                copy[index] = "Gold Medal"
            elif i == 1:
                copy[index] = "Silver Medal"
            elif i == 2:
                copy[index] = "Bronze Medal"
            else:
                copy[index] = str((i+1))
        return copy

    def convert_to_string(self, list: List[int]) -> List[str]:
        return [str(i) for i in list]

        