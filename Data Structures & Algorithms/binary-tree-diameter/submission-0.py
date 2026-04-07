# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0  # 用来记录全局最大直径

        def dfs(curr):
            if not curr:
                return 0
            
            # 递归计算左右子树的高度
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            # 在每个节点处，更新最大直径
            # 直径 = 左高度 + 右高度
            self.res = max(self.res, left + right)
            
            # 返回当前节点的高度给上层使用
            return 1 + max(left, right)

        dfs(root)
        return self.res
        