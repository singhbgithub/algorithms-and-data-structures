# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """Iterative approach."""
        res = []
        rights = []
        p = root
        while p:
            res.append(p.val)
            if p.left and p.right:
                rights.append(p.right)
            p = p.left or p.right or (rights and rights.pop())
        return res
