class Solution:
    def missingNumber(self, nums: List[int]) -> int:
            res = len(nums)  # 初始值设为 n，因为下标循环只能到 n-1
            for i, num in enumerate(nums):
                res ^= i ^ num
            return res