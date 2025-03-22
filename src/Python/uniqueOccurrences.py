
#using count is very slow, it does O(N) every single time ran
# because of that this code is O(n^2)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr: 
            c = arr.count(i)
            d[i] = c
        
        values = list(d.values())
        print(values)
        for v in values:
            if values.count(v) > 1:
                return False

        return True

#this one is faster with O(N)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            print(f"Counting {i}: current count {d[i]}")

        values = list(d.values())
        print(f"All counts: {values}")

        unique_counts = set(values)
        print(f"Unique counts: {unique_counts}")

        return len(values) == len(unique_counts)
