class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        lens = len(digits)
        
        for i in range(lens-1,-1,-1):
            total = digits[i] + carry
            res.append(total%10)
            carry = total//10
        if carry == 1:
            res.append(1)
        return res[::-1]