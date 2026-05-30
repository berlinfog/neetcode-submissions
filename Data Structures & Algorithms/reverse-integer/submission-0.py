class Solution:
    def reverse(self, x: int) -> int:
        sgn = 1 if x >=0 else -1
        x = x if x >= 0 else -x
        res = 0
        while x > 0:
            dgt = x % 10
            x = x//10
            res = res * 10 + dgt
        res *= sgn
        if res < (-2**31) or res > (2**31-1):
            return 0
        return res
    
    
       