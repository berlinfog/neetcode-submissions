# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def reOrg(root):
            if not root:
                return []
            return ([] if not root.left else reOrg(root.left)) + [root.val] + ([] if not root.right else reOrg(root.right))
        lst = reOrg(root)
        return lst[k-1]