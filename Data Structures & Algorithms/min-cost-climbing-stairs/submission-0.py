class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # prev2 代表走到 i-2 阶的最小总花费
        # prev1 代表走到 i-1 阶的最小总花费
        # 题目说可以从第 0 或第 1 阶开始，所以初始站在那里的花费是 0
        prev2, prev1 = 0, 0
        
        # 我们要走到楼梯顶端，也就是越过最后一个台阶，所以是 len(cost) + 1
        for i in range(2, len(cost) + 1):
            # 走到当前 i 阶的最小花费，就是比较两种方案哪个更省钱：
            # 方案 A：从 i-1 跨一步过来（之前累计的花费 + 踩跳板的花费 cost[i-1]）
            # 方案 B：从 i-2 跨两步过来（之前累计的花费 + 踩跳板的花费 cost[i-2]）
            curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            
            # 滚动变量，继续往上走
            prev2, prev1 = prev1, curr
            
        return prev1