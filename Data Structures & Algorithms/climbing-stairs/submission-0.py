class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        # for 3 1+2 1+1+1 2+1
        # for 4 1+1+1+1 1+2+1 1+1+2 2+1+1 2+2 dp[3]+dp[1]
        for i in range(2,n+1):
            dp[i] = dp[i-1]+ dp[i-2]
        return dp[n]