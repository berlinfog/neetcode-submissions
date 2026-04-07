class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        chars = {"+","-","*","/"}
        for i in tokens:
            if i not in chars:
                stack.append(int(i))
            else:
                res2 = stack.pop()
                res1 = stack.pop()
                if   i == "+":
                    stack.append(res1 + res2)
                elif i == "-":
                    stack.append(res1 - res2)
                elif i == "*":
                    stack.append(res1 * res2)
                else:
                    stack.append(int(res1 / res2))
        return stack[0]
# 9 4 -
