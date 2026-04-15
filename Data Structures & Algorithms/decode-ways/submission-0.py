class Solution:
    def numDecodings(self, s: str) -> int:
        # 如果字符串直接以 '0' 开头，无论如何也解不出，直接白给
        if not s or s[0] == '0':
            return 0
            
        n = len(s)
        # dp[i] 代表前 i 个字符 (即 s[0:i]) 的解码方法数
        dp = [0] * (n + 1)
        
        # Base Case
        dp[0] = 1  # 虚拟的空字符串，算作 1 种方法（为了给双字符解码做铺垫）
        dp[1] = 1  # 上面已经排除了开头是 '0' 的情况，所以第 1 个字符必定有 1 种解法
        
        # 从第 2 个字符开始填表
        for i in range(2, n + 1):
            # 方案 A：单字符解码 (跨 1 步)
            # 只要当前这个字符(s[i-1])不是 '0'，就能继承昨天的解法
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
                
            # 方案 B：双字符解码 (跨 2 步)
            # 提取前一个和当前字符拼成两位数
            two_digit = int(s[i - 2 : i])
            # 只要在这个合法的范围内，就能继承前天的解法
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
                
        return dp[n]