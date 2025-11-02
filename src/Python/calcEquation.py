
class Solution:
    def calcEquation(self, equations, values, queries):
        g = defaultdict(dict)

        for (a, b), val in zip(equations, values):
            g[a][b] = val
            g[b][a] = 1 / val

        res = []

        def find(a, b, visited):
            if a not in g or b not in g:
                return -1.0
            if a == b:
                return 1.0
            visited.add(a)
            for nei, val in g[a].items():
                if nei in visited:
                    continue
                sub = find(nei, b, visited)
                if sub != -1.0:
                    return val * sub
            return -1.0

        i = 0
        while i < len(queries):
            a = queries[i][0]
            b = queries[i][1]
            num = g.get(a, {}).get(b, -1.0)
            if num == -1.0:
                num = find(a, b, set())
            res.append(float(num))
            i += 1

        print(res)
        print(g)
        return res
