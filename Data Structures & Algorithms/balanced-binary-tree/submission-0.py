# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node): # 1. 这里不需要 self
            if not node:
                return 0
            
            left = dfs(node.left)   # 2. 直接调用 dfs
            right = dfs(node.right)
            
            # 3. 核心判断：
            # 如果左边不平衡 (-1)
            # 或者右边不平衡 (-1)
            # 或者“我”这一层不平衡 (左右差 > 1)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            # 4. 如果是平衡的，正常返回高度
            return max(left, right) + 1
        
        # 5. 最后判断 dfs 的结果是不是 -1
        return dfs(root) != -1
        
        