# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """Iterative."""
        r = []
        s = [root]
        while s:
            node = s.pop()
            while node:
                r.append(node.val)    # act on current
                s.append(node.right)  # defer right
                node = node.left      # go left
        return r
