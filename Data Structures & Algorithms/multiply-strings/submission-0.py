class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 11
        # 22
        l1 = len(num1) -1
        l2 = len(num2) -1
        res = 0
        l1s = 1
        l2s = 1
        for i in range(l1,-1,-1):
            l2s = 1
            for j in range(l2,-1,-1):
                res += l1s*(ord(num1[i])-ord('0')) * l2s* (ord(num2[j])-ord('0'))
                l2s *= 10
            l1s *= 10
        return str(res)
                
        
