class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        l,r = 0, lens-1
        while l <= r:
            m = (r-l)//2 + l
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m -1
            else:
                l = m + 1
        return -1