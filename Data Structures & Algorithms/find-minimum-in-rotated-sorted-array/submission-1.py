class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # 如果中间值比最右边大，说明左半部分是正常的升序，
            # 最小值肯定在右半部分（那个断层处）
            if nums[mid] > nums[r]:
                l = mid + 1
            # 否则，最小值在左半部分（包含 mid 自己）
            else:
                r = mid
                
        return nums[l]