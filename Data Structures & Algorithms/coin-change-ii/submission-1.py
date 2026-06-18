class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] 表示凑成金额 i 的组合数
        dp = [0] * (amount + 1)
        dp[0] = 1 # 凑出 0 元的组合数为 1
        
        # 核心：必须先遍历硬币，再遍历金额！
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                
        return dp[amount]