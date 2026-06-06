# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root.left and not root.right:
            if root.val==0: return False
            return True
        left=self.evaluateTree(root.left)
        right=self.evaluateTree(root.right)
        if root.val==2:
            return left or right
        return left and right