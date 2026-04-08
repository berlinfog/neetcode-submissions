import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. 统计频率：{"A": 3, "B": 2...}
        count = Counter(tasks)
        
        # 2. 建立大顶堆（Python默认小顶堆，所以存负数）
        # 我们只关心频率，不关心任务名字
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        # queue 存储：[剩余频率, 可以重新入堆的时间点]
        queue = deque() 
        
        while maxHeap or queue:
            time += 1
            
            if maxHeap:
                # 拿出当前最高频的任务执行
                cnt = heapq.heappop(maxHeap) + 1 # 频率减1（负数加1等于绝对值减1）
                if cnt != 0:
                    # 还没做完，进入冷却队列
                    # 解禁时间 = 当前时间 + n
                    queue.append([cnt, time + n])
            
            # 检查队列头部的任务是否冷却结束
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
                
        return time