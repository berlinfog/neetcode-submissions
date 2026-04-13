class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        # dp 数组和 nums 一样长
        dp = [0] * len(nums)
        
        # 初始状态：
        dp[0] = nums[0]                  # 只有一栋房子，只能抢它
        dp[1] = max(nums[0], nums[1])    # 有两栋房子，抢钱多的那栋
        
        # 状态转移：
        for i in range(2, len(nums)):
            # 方案 A：抢当前这栋 nums[i] + 前天抢的钱 dp[i-2]
            # 方案 B：不抢当前这栋，直接拿昨天抢的钱 dp[i-1]
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            
        return dp[-1]