class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 树的另一个铁律：n个点的树，边数必须正好是 n - 1
        # 如果边数不对，要么有环，要么不连通，直接返回 False
        if len(edges) != n - 1:
            return False

        # 建邻接表（无向图，双向加边）
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:
                # 如果邻居是带我来的亲爹，直接跳过
                if neighbor == parent:
                    continue
                # 如果邻居不是亲爹，而且已经访问过了，说明绕回来了，有环！
                if neighbor in visited:
                    return False
                # 递归往下走，把当前节点当成邻居的 parent 传下去
                if not dfs(neighbor, node):
                    return False

            return True

        # 从 0 号节点开始跑，规定 0 号节点的亲爹是 -1
        # 如果从 0 出发能顺利走完，并且访问到了所有的点（len(visited) == n），那就是一棵完美的树
        return dfs(0, -1) and len(visited) == n