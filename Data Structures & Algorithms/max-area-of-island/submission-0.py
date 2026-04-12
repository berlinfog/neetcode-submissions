class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0

        def dfs(i,j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] ==0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i-1,j) + dfs(i,j-1) + dfs(i+1,j) + dfs(i,j+1)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))
        return res
        