from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # check the pre array and order it as a list
        # and then to see whether it has loop or just hashset to see 
        # but how to figure [1,2] [1,3] [3,1]
        # so we need a graph [][] to record 


        # 创建邻接表：key 是先修课，value 是它指向的所有后修课列
        # 1. 顺着你的思路建图：key 是先修课，value 是它指向的所有后修课列表
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[pre].append(crs)

        # visiting 记录当前 DFS 路径上的课（用于抓死循环）
        visiting = set()
        # visited 记录已经确定安全的课（用于跳过重复计算，免得超时）
        visited = set()

        def dfs(crs):
            # 如果这门课已经在当前路径里了，说明转回来了，抓到环！
            if crs in visiting:
                return False
            # 如果这门课之前已经安全探测过了，直接绿灯放行
            if crs in visited:
                return True

            # 标记当前课正在被访问
            visiting.add(crs)

            # 递归去上它后面依赖的所有课
            for next_crs in graph[crs]:
                if not dfs(next_crs):
                    return False  # 只要后面有一条路走入死胡同，全盘皆输

            # 这一路所有的课都顺利修完了，把当前课从路径中移出
            visiting.remove(crs)
            # 永久标记这门课为“安全课”
            visited.add(crs)
            return True

        # 因为图可能是不连通的（比如有几门课自己成一个孤岛），所以必须每门课都当成起点跑一遍
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
            