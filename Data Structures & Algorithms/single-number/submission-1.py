class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
        # res = set()
        # for i in nums:
        #     if i not in res:
        #         res.add(i)
        #     else:
        #         res.remove(i)
        # return res.pop()