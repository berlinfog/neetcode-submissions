class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 初始化全局最大值，以及当前的最大值和最小值
        res = nums[0]
        curMax, curMin = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            
            # 把三个备选项列出来：
            # 1. 当前数字自己另起炉灶 (n)
            # 2. 跟前面的最大值连起来 (n * curMax)
            # 3. 跟前面的最小值连起来 (n * curMin，也就是赌一把负负得正)
            options = (n, n * curMax, n * curMin)
            
            curMax = max(options)
            curMin = min(options)
            
            # 随时更新全局最大纪录
            res = max(res, curMax)
            
        return res