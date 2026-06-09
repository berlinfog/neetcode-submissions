class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dq = deque()
        fresh_count = 0  # 💡 新增：记录新鲜橘子的总数
        
        # 1. 初始遍历：找烂橘子，数新鲜橘子
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    dq.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
                    
        # 💡 特判：如果一开始就没有新鲜橘子，直接返回 0
        if fresh_count == 0:
            return 0
            
        dire = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        res = 0
        
        # 💡 关键修改：只有当队列不为空，且还有新鲜橘子时，才继续扩散
        while dq and fresh_count > 0:
            templ = len(dq)
            for temp in range(templ):
                i, j = dq.popleft()
                for dr, dl in dire:
                    r = i + dr
                    c = j + dl
                    
                    # 注意这里的判断条件：只感染新鲜橘子(1)
                    if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 1:
                        continue
                    
                    grid[r][c] = 2
                    dq.append((r, c))
                    fresh_count -= 1  # 💡 每烂一个，新鲜橘子就少一个
                    
            res += 1  # 这一分钟过完，时间 +1
            
        # 3. 结算：如果还有新鲜橘子没烂完，说明有孤岛，返回 -1
        return res if fresh_count == 0 else -1