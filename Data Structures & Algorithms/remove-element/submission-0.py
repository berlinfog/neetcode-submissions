class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # 慢指针，表示下一个不等于 val 的元素应该放的位置
        
        # j 就是你的快指针，用来遍历整个数组
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                
        # 题目要求返回最后数组的长度，正好就是慢指针 i 的值
        return i