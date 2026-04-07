class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        # 初始化两个数组，长度与输入相同
        leftMax = [0] * n
        rightMax = [0] * n
        
        # 1. 从左向右遍历，填充 leftMax
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
            
        # 2. 从右向左遍历，填充 rightMax
        rightMax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
            
        # 3. 遍历每个位置，计算积水
        total_water = 0
        for i in range(n):
            # 取左右两边最高柱子中较短的那个，减去当前柱子的高度
            # 这里的 min(leftMax[i], rightMax[i]) 就是木桶的“短板”
            water_at_i = min(leftMax[i], rightMax[i]) - height[i]
            total_water += water_at_i
            
        return total_water    