class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxr = 0
        for i,j in enumerate(nums):
            if i > maxr:
                return False
            maxr = max(maxr,i+j)
            if maxr >= (len(nums) - 1):
                return True
        return True