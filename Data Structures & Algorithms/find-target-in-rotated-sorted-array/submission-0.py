class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # 比较 m 和 r 来确定有序部分
            if nums[m] <= nums[r]:
                # 说明右半部分 [m, r] 是升序有序的
                if nums[m] < target <= nums[r]:
                    l = m + 1 # target 在右边有序区间内
                else:
                    r = m - 1 # 否则去左边找
            else:
                # 说明左半部分 [l, m] 是升序有序的 (因为断层在右边)
                if nums[l] <= target < nums[m]:
                    r = m - 1 # target 在左边有序区间内
                else:
                    l = m + 1 # 否则去右边找
                    
        return -1