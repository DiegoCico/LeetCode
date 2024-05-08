class Solution:
    def partitionString(self, s: str) -> int:
        new = []
        combination = ""
        for i in s:
            if i in combination:
                new.append(combination)
                combination = i
            else:
                combination += i

        if combination:
            new.append(combination)

            print(combination)
        print(new)
        return len(new)
