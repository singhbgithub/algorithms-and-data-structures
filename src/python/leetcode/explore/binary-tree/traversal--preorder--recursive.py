# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """Recursive."""
        if root is None:
            return []
        l = self.preorderTraversal(root.left)
        r = self.preorderTraversal(root.right)
        return [root.val] + l + r
