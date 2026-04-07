class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l r and mid = (l+r)//2
        # if nums[l] < mid < nums[r]
        return min(nums)