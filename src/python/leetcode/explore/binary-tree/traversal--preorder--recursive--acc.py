# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """Recursive - accumulator."""

        def preorderWithAcc(node: TreeNode, acc: List[int]):
            if node is not None:
                acc.append(node.val)
                preorderWithAcc(node.left, acc)
                preorderWithAcc(node.right, acc)

        acc = []
        preorderWithAcc(root, acc)
        return acc