from collections import deque
import math

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        # 1. 第一步：把所有的宝箱 (0) 找出来，全部塞进队列作为“波纹”的起点
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    
        # 2. 第二步：多源 BFS 开始扩散
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while q:
            r, c = q.popleft() # 弹出一个当前点
            
            # 向四个方向探索
            for dr, dc in directions:
                row, col = r + dr, c + dc
                
                # 💡 剪枝核心：
                # 如果越界了，或者是水(-1)，或者**已经被别人抢先访问过了(不是 INF)**，直接跳过！
                if (row < 0 or row >= ROWS or 
                    col < 0 or col >= COLS or 
                    grid[row][col] != 2147483647):
                    continue
                
                # 💡 原地修改：因为是 BFS，最先到达这里的波纹肯定是最短距离！
                # 它的距离 = 传播它过来的那个点的距离 + 1
                grid[row][col] = grid[r][c] + 1
                
                # 把新感染的陆地加入队列，作为下一波的起点
                q.append((row, col))