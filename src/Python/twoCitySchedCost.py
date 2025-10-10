class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s = 0
        costs.sort(key = lambda x : x[0] - x[1])
        n = len(costs)//2 
        for i in range(0,n):
            s += costs[i][0] + costs[n+i][1]
        return s 