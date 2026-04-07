class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(','{','[']

        for i in s:
            if i in left:
                stack.append(i)
            else:
                if stack:
                    if   i == ')' and stack[-1] == '(':
                        stack.pop()
                    elif i == ']' and stack[-1] == '[':
                        stack.pop()
                    elif i == '}' and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return len(stack) == 0