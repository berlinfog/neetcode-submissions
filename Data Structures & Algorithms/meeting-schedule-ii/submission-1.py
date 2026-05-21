"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x : x.start)
        rooms = []
        if len(intervals) == 0:
            return 0
        heapq.heappush(rooms,intervals[0].end)

        for i in range(1,len(intervals)):
            tmp = intervals[i]

            if tmp.start >= rooms[0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms,tmp.end)
        return len(rooms)