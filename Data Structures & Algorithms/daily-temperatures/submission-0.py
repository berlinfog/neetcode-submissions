class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # 这里只存下标 index
        
        for i, t in enumerate(temperatures):
            # 当当前温度 > 栈顶下标对应的温度时
            while stack and t > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            
            stack.append(i)
            
        return res