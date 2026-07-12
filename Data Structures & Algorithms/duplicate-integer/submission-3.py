class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for i in nums:
            res.add(i)
        return len(res) != len(nums)