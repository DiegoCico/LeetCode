class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            left = cost[i-1] + cost[i]
            right = cost[i-2] + cost[i]
            cost[i] = min(left, right)
        
        return min(cost[len(cost)-1],cost[len(cost)-2])