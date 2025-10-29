class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result = []
        print(target)
        
        def backtrack(curr, path):
            if curr == target:
                result.append(list(path))
                return
            
            for node in graph[curr]:
                path.append(node)
                backtrack(node, path)
                path.pop()


        path = [0]
        backtrack(0,path)

        return result