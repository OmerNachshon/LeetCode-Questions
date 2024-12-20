"""
Given a binary tree, determine if it is
height-balanced
.
"""
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return 1+max(left,right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left-right) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)
