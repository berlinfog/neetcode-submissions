from collections import deque
class Solution:
    def checkValidString(self, s: str) -> bool:
        res = []
        star = []
        for c in range(len(s)):
            tmp = s[c]
            if tmp == '(':
                res.append(c)
            elif tmp == '*':
                star.append(c)
            else:
                if res:
                    res.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while res and star:
            if star[-1] < res[-1]:
                return False
            star.pop()
            res.pop()
        return len(res) == 0