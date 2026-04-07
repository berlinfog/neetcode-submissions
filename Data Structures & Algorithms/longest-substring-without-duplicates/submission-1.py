class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lens = len(s)
        if lens == 0:
            return 0
        l,r = 0,0
        temp = set()
        res = 1
        temp.add(s[l])
        while r < lens-1:
            r += 1
            while s[r] in temp:
                temp.remove(s[l])
                l += 1
            res = max(res,r-l+1)
            temp.add(s[r])
        return res
