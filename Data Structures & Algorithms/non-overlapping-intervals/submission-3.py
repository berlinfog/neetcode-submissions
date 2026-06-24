class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res = 0
        temp =[]
        for i in intervals:
            if temp and temp[-1][1] > i[0]:
                res += 1
                temp[-1] = temp[-1] if temp[-1][1] <i[1] else i
            else:
                temp.append(i)
        return res