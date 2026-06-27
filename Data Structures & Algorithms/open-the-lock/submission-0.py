from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 把 deadends 变成 set，这样 O(1) 查询快得多
        dead = set(deadends)
        
        # 边界情况：如果起点就在死路里，或者终点在死路里（题目说终点不在，保险起见看起点就行）
        if "0000" in dead:
            return -1
            
        # 队列里存 (当前锁的状态, 当前转动的步数)
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        
        while queue:
            curr, steps = queue.popleft()
            
            # 抓到目标，直接返回
            if curr == target:
                return steps
                
            # 尝试拨动 4 个轮子
            for i in range(4):
                digit = int(curr[i])
                
                # 每个轮子有两种拨法：+1 或者 -1（注意处理 0 和 9 的回绕）
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    # 拼出新的字符串状态
                    nxt = curr[:i] + str(new_digit) + curr[i+1:]
                    
                    # 如果这个状态既没走过，也不是死路，就塞进队列
                    if nxt not in visited and nxt not in dead:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))
                        
        # 队列空了都没找到，说明被死路堵死了，根本去不了
        return -1