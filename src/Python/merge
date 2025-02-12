class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        l = []
        i = 0
        while i < len(intervals):
            if i != len(intervals)-1:
                if intervals[i][1] > intervals[i+1][0]:
                    l.append([intervals[i][0], intervals[i+1][1]])
                    i += 1
                else:
                    l.append(intervals[i])
            else:
                l.append(intervals[i])
            i+=1
            
        return l
        