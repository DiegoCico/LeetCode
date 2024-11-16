class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
            f = [*map(itemgetter(1), Counter(tasks).most_common())]
            m = max(f)
            return max((m - 1) * (n + 1) + f.count(m), len(tasks))  