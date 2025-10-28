class Solution:
    def trap(self, height: List[int]) -> int:
        c = 0
        interval = []
        left = 0

        for i in range(len(height)):
            h = height[i]
            if not interval and h > 0:
                interval.append((i, h))
                left = h
            elif interval:
                interval.append((i, h))

                print(f"interval: {[x[1] for x in interval]}")

                if h >= left:
                    trapped = 0
                    for j in range(interval[0][0] + 1, i):
                        water = left - height[j]
                        if water > 0:
                            trapped += water
                            c += water
                            print(f"  trapped {water} at index {j}")
                    print(f"filled between {interval[0][0]} and {i}: +{trapped}, total={c}")
                    interval = [(i, h)]  
                    left = h

            print(f"current total: {c}\n")

        if interval:
            print("Right-side cleanup:")
            right_max = 0
            for j in range(len(interval)-1, -1, -1):
                right_max = max(right_max, interval[j][1])
                water = right_max - interval[j][1]
                if water > 0:
                    c += water
                    print(f"  trapped {water} at index {interval[j][0]}")
            print(f"final total: {c}")

        return c


