"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest = [0]
        def diameter(root):
            if not root:
                return 0
            l = diameter(root.left)
            r = diameter(root.right)
            curr = l + r
            largest[0] = max(largest[0],curr)
            return 1+max(l,r)

        diameter(root)
        return largest[0]


