class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        # 1 7 6 5 2 3
        # use a ? data structure to record subset and its min,max,but
        # how to use O(1) 
        # iterate and add to this structure
        # iterate this ? data structure and calculate max-min+1
        for i in nums:
            if (i-1) not in numset:
                length = 0
                while (i + length) in numset:
                    length += 1
                longest = max(longest,length)
        return longest