class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 情况 1：两个都是空，那肯定一样
        if not p and not q:
            return True
        
        # 情况 2：其中一个是空，或者值不一样，那肯定不一样
        # 注意：走到这里说明 p 和 q 至少有一个不是 None
        if not p or not q or p.val != q.val:
            return False
        
        # 情况 3：根节点一样，那就得看左右子树是不是都一样
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)