class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        # 统计 t 中需要的字符
        need = {}
        for c in t: need[c] = need.get(c, 0) + 1
        
        window = {}
        have, required = 0, len(need)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            # 如果当前字符是需要的，且数量正好达到标准
            if char in need and window[char] == need[char]:
                have += 1
                
            # 当满足所有条件时，尝试收缩左边界
            while have == required:
                # 更新最小窗口结果
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                # 弹出左侧字符
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""