class KthLargest:
    lst = []
    k = 0
    def __init__(self, k: int, nums: List[int]):
        self.lst = sorted(nums)
        self.k = k 
    def add(self, val: int) -> int:
        if val in self.lst:
            idx = self.lst.index(val)
            self.lst.insert(idx,val)
        else:
            l = 0
            r = len(self.lst)-1
            m = 0
            while l <= r:
                m = (l + r) // 2
                if self.lst[m] > val:
                    r = m - 1 # 放心跨过去，l 会帮你守住位置
                else:
                    l = m + 1
            self.lst.insert(l,val)
        return self.lst[len(self.lst)-self.k]

