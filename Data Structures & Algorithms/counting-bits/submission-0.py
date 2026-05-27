class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(1,n+1):
            if i & 1 == 0: # like 2
                res[i] = res[i>>1]
            else:
                res[i] = res[i>>1] + 1
        return res


