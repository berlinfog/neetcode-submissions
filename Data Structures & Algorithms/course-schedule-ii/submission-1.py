from collections import defaultdict


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. 建图逻辑一模一样
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[pre].append(crs)

        visiting = set()
        visited = set()

        # 用来存最终的全局路径
        res = []

        def dfs(crs):
            if crs in visiting:
                return False  # 有环，完蛋
            if crs in visited:
                return True  # 已经安全访问过，直接跳过，不用重复加进 res

            visiting.add(crs)

            for next_crs in graph[crs]:
                if not dfs(next_crs):
                    return False

            visiting.remove(crs)
            visited.add(crs)

            # 🔥 核心改动：这门课的所有后修课都搞定了，它安全了！
            # 把它塞进结果里。它会自然而然地形成正确的先后顺序。
            res.append(crs)
            return True

        # 依然是老规矩，每门课当起点扫一遍
        for i in range(numCourses):
            if not dfs(i):
                return []  # 一旦有环，说明无法修完，按照题目要求返回空列表 []

        # 如果建图是 crs -> pre（即通过后修课找先修课），res 出来就是对的。
        # 如果建图是 pre -> crs（先修课指向后修课），把 res 倒过来返回即可：return res[::-1]
        # 根据我们上面 graph[pre].append(crs) 的建图逻辑，res 出来的顺序刚好就是正确的修课顺序。
        return res[::-1]