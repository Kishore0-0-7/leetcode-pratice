# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        lst=[]
        if root:
            lst.extend(self.inorderTraversal(root.left))
            lst.append(root.val)
            lst.extend(self.inorderTraversal(root.right))
        return lst