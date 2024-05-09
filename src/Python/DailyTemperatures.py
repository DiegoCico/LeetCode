class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                days[prev_index] = i - prev_index
            stack.append(i)
            days.append(0)

        return days
