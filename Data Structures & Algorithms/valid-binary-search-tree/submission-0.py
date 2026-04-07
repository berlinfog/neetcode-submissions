# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bstComp(root,sml,lgr):
            if not root:
                return True
            if root.val < lgr and root.val > sml:
                return bstComp(root.left,sml,root.val) and bstComp(root.right,root.val,lgr)
            else:
                return False
        return bstComp(root,-1001,1001)