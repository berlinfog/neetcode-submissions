class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = set()
        for i in nums:
            if i not in res:
                res.add(i)
            else:
                res.remove(i)
        return res.pop()