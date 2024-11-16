class Solution:
    def countSteppingNumbers(self, low, high):
        def backtrack(path):
            if len(path) > len(str(high)) or (len(path) > 1 and path[0] == "0"): return
            if path and (low <= int(path) <= high): res.append(int(path))

            for i in range(10):
                if path == "" or abs(int(path[-1]) - i) == 1:
                    backtrack(path+str(i))

        res = []
        backtrack("")
        return sorted(res)
