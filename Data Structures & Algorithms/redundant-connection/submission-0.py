class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # 节点编号是从 1 到 n
        n = len(edges)
        parent = [i for i in range(n + 1)]
        
        # 查找根节点（带路径压缩优化）
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        # 合并两个节点
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False # 如果根节点相同，说明成环了
            
        for u, v in edges:
            # 如果 u 和 v 已经连通，说明当前这条边就是多余的
            if not union(u, v):
                return [u, v]