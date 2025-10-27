class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1

        return count
