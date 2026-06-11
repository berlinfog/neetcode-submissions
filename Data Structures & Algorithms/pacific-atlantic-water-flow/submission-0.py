class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
            
        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        # r: row, c: col
        def dfs(r, c, reachable_set):
            # 标记当前格子已被这支搜救队探明
            reachable_set.add((r, c))
            
            # 向上下左右四个方向爬山
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # 检查边界条件
                if 0 <= nr < m and 0 <= nc < n:
                    # 关键：只有下个格子比当前格子【高或等高】，搜救队才能爬上去
                    # 同时确保下个格子没被当前搜救队重复访问过
                    if (nr, nc) not in reachable_set and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, reachable_set)

        # 1. 左右两边界出发
        for r in range(m):
            dfs(r, 0, pacific_reachable)     # 左边界 -> 太平洋
            dfs(r, n - 1, atlantic_reachable) # 右边界 -> 大西洋
            
        # 2. 上下两边界出发
        for c in range(n):
            dfs(0, c, pacific_reachable)     # 上边界 -> 太平洋
            dfs(m - 1, c, atlantic_reachable) # 下边界 -> 大西洋
            
        # 3. 找出两军会师的交集格子
        res = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    res.append([r, c])
                    
        return res