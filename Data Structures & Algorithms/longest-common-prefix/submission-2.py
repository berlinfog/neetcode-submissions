class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tmp = strs[0]
        if len(strs) == 1:
            return tmp
        for i in strs[1:]:
            while i[:len(tmp)] != tmp:
                tmp = tmp[:-1]
                if not tmp:
                    return ""
        return tmp