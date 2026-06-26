class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        # 1. 必须按 start 排序，确保会议是按时间先后看的
        intervals.sort(key = lambda x: x.start)
        
        # 2. 记录第一个会议的结束时间
        prev_end = intervals[0].end
        
        # 3. 从第二个会议开始检查
        for i in range(1, len(intervals)):
            curr = intervals[i]
            # 如果当前会议开始时间 < 上一个会议结束时间，说明冲突了
            if curr.start < prev_end:
                return False
            # 更新最晚的结束时间
            prev_end = max(prev_end,curr.end)
            
        return True