class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        baseline_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                baseline_satisfied += customers[i]
        
        max_additional_satisfied = 0
        current_window_satisfied = 0

        for i in range(minutes):
            if grumpy[i] == 1:
                current_window_satisfied += customers[i]
        
        max_additional_satisfied = current_window_satisfied
        
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                current_window_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                current_window_satisfied -= customers[i - minutes]
            max_additional_satisfied = max(max_additional_satisfied, current_window_satisfied)
        
        return baseline_satisfied + max_additional_satisfied
