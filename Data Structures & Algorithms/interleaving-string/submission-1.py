class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # 出发点，空字符串显然可以匹配空字符串
        dp[0][0] = True
        
        # 1. 初始化第一列：只用 s1 能否匹配 s3 的前缀（只能一路向下走）
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
            
        # 2. 初始化第一行：只用 s2 能否匹配 s3 的前缀（只能一路向右走）
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
            
        # 3. 填充剩余网格
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 只要上面能走下来，或者左边能走过来
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                           (dp[i][j-1] and s2[j-1] == s3[i+j-1])
                           
        return dp[m][n]