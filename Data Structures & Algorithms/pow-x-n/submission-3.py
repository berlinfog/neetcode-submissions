class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.myPow(x,-n)
        if n == 0:
            return 1.0
        half = self.myPow(x,n//2)
        if n % 2 == 1: 
            return half * half * x
        else:
            return half * half