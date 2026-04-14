class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        # 1. 初始化表：dp[i][j] 代表 s[i...j] 是否是回文
        dp = [[False] * n for _ in range(n)]
        # 所有长度为 1 的子串都是回文
        for i in range(n):
            dp[i][i] = True
            
        max_len = 1
        begin = 0
        
        # 2. 开始填表
        # i 必须倒着走，因为 i 依赖 i+1
        for i in range(n - 1, -1, -1):
            # j 只要在 i 右边就行
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # 长度小于等于 3 或者是中间部分也是回文
                    if j - i < 3 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                
                # 3. 维护最长记录
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    begin = i
                    
        return s[begin : begin + max_len]