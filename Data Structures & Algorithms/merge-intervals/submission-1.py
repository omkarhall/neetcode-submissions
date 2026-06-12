class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        res = []
        while i <= len(intervals) - 1:
            start = intervals[i][0]
            end = intervals[i][1]
            while i <= len(intervals) - 2 and end >= intervals[i + 1][0]:
                end = max(end, intervals[i+1][1])
                i += 1
            res.append([start, end])
            i += 1
        return res