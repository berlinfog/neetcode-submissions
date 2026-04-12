class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def dfs(i,temp):
            if i == len(digits):
                res.append(temp)
                return res
            num = digits[i]
            for j in phone[num]:
                dfs(i+1,temp+j)
            
        dfs(0,"")
        return res
