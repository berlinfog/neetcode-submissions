class Solution:
    def isHappy(self, n: int) -> bool:
        rec = set()
        while n != 1 and n not in rec:
            rec.add(n)
            total = 0
            while n > 0:
                digit = n%10
                total += digit * digit
                n //=10
            n = total
        return n == 1

# 7 49 97 130 1000