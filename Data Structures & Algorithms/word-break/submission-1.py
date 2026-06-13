class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp 数组多开一位，代表越过字符串结尾的"终点"状态
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True 
        
        # i 从最后一个字符倒着往前走
        for i in range(len(s) - 1, -1, -1):
            # 遍历字典里的每一个单词
            for w in wordDict:
                # 检查：1. 长度没越界 2. 刚好匹配得上
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    # 继承匹配成功后的那个位置的状态
                    dp[i] = dp[i + len(w)]
                
                # 只要有一种匹配方式能让 dp[i] 变成 True，就没必要再试其他单词了
                if dp[i]:
                    break
                    
        # 最后返回起点，看看从头到尾能不能完美拆分
        return dp[0]