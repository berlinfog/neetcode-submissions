class MinStack:
    def __init__(self):
        # 初始化主栈用于存数据，min_stack用于存当前主栈状态下的最小值
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # 主栈直接压入数据
        self.stack.append(val)
        
        # 如果min_stack为空，或者新的val小于等于当前的最小值
        # 就将新的val也压入min_stack，更新全局最小值
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # 如果弹出的元素正是当前的最小值，min_stack也需要同步弹出
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # 返回主栈的栈顶元素
        return self.stack[-1]

    def getMin(self) -> int:
        # 返回min_stack的栈顶元素，即当前栈中的最小值
        return self.min_stack[-1]