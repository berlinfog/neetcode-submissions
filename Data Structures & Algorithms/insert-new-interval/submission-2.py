from collections import heapq
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if newinterval[1] < intervals[0][0] then add to res
        # if newinterval[0] > intervals[-1][-1] then add to res

        # then need to check where to insert
        # if interval[0] > newinterval[1]
        res = []
        i = 0
        n = len(intervals)
        
        # 1. 插入所有在新区间之前的区间
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        # 2. 合并所有重叠的区间
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        
        # 3. 插入剩下的区间
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res
            
                