"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = sorted([i.start for i in intervals])
        endTimes = sorted([i.end for i in intervals])
        max_count, count = 0, 0
        i, j = 0, 0
        while i < len(startTimes):
            if startTimes[i] < endTimes[j]:
                count += 1
                max_count = max(max_count, count)
                i += 1
            else:
                count -= 1
                j += 1
        return max_count


