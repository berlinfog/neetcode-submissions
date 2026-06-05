class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # 1. 构建邻接表
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        count = 0
        
        # 2. 内层 DFS 函数
        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        # 3. 外层 for 循环
        for i in range(n):
            if i not in visited:
                count += 1       # 发现一个新的连通分量
                visited.add(i)   # 标记起点
                dfs(i)           # 通过 DFS 标记所有同属于这个分量的点
                
        return count