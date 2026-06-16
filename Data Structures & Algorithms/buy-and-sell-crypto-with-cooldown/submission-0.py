class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pl = len(prices)
        if pl <= 1:
            return 0
            
        # dp[i][0] 表示当天结束手里【没有】股票的最大利润
        # dp[i][1] 表示当天结束手里【持有】股票的最大利润
        dp = [[0 for _ in range(2)] for _ in range(pl)]
        
        # 第 0 天初始状态
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        # 第 1 天初始状态（因为买入不能看 i-2，单独算）
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], -prices[1]) # 第1天买，前面只能是空手
        
        for i in range(2, pl):
            # 今天没股票：要么昨天就没股票，要么今天刚卖了
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            
            # 今天有股票：要么昨天就有，要么今天刚买
            # 关键：如果今天买，昨天必须是冷冻/空手，所以能用来买的本金来自前天 dp[i-2][0]
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            
        return dp[pl-1][0]