class Solution:
    def minSwaps(self, data: List[int]) -> int:
        count = data.count(1)
        curr = data[:count].count(1)
        ans = count - curr
        for i in range(count, len(data)):
            if data[i - count] == 1: curr -= 1
            if data[i] == 1: curr += 1
            ans = min(ans, count - curr)
        return ans 