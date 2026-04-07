class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 10000 * 10000
        temp = set()
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                return i