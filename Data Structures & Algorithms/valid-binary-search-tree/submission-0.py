# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):

        def check(node, low, high):
            if node is None:
                return True

            # node must be between low and high
            if node.val <= low or node.val >= high:
                return False

            # left = smaller
            if not check(node.left, low, node.val):
                return False

            # right = bigger
            if not check(node.right, node.val, high):
                return False

            return True

        return check(root, float("-inf"), float("inf"))