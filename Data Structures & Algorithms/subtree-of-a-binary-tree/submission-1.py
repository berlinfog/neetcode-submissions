# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case 1: 如果主树空了，肯定找不到了
        if not root:
            return False
        
        # 逻辑 A: 检查当前这两个根节点开始，是不是“相同的树”
        if self.isSameTree(root, subRoot):
            return True
        
        # 逻辑 B: 如果当前不像，就去左边找，或者去右边找（这就是你说的“比一比”）
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # 这是你刚才写的那个“套在里面”的辅助函数
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)