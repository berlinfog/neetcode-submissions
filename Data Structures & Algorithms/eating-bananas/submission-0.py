class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. 确定二分查找的范围
        left, right = 1, max(piles)
        res = right # 默认最大速度肯定能吃完
        
        while left <= right:
            k = (left + right) // 2
            
            # 2. 计算以速度 k 吃完所有香蕉需要的总时间
            total_time = 0
            for p in piles:
                # 向上取整的优雅写法
                total_time += (p + k - 1) // k 
            
            # 3. 判断并收缩区间
            if total_time <= h:
                # 说明速度还可以再慢一点，记录当前速度并往左找
                res = k
                right = k - 1
            else:
                # 说明速度太慢了，得加点速
                left = k + 1
                
        return res